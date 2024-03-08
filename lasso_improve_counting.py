from bloom_filter import *
from rappor import* 
import numpy as np
import math
from sklearn.linear_model import Lasso
from get_data import *
def improved_counting(epsilon, p, q):
    
    data=get_data('test_data.csv',0)

    num_interests = len(data)  # 兴趣总数
    random.seed()

    f = 1.0 / (1.0 + math.exp(epsilon))
    c = [0] * 18  # 初始化 c 列表
    arr_all = [0] * num_interests  # 初始化 arr_all 列表   
    
    count_ = []
    for i in range(num_interests):
        item = data[i]
        count_.append(item[1])

    for i in range(num_interests):
        for j in range(count_[i]):
            rappor(f, p, q, i, c, arr_all)
    
    # 计算 tij
    t = []
    for tij, ni in zip(c, arr_all):
        tij_estimate = (tij - (p + 0.5 * f * q - 0.5 * f * p) * ni) / ((1 - f) * (q - p))
        t.append(tij_estimate)

    # 输出计算后的结果
    for i, tij_estimate in enumerate(t):
        print(f"t{i+1} = {tij_estimate}")

    # 使用 Lasso 回归改进计数
    X = create_design_matrix(c, num_interests)

    # 构建响应变量 Y
    Y = np.array(t)

    # 初始化 Lasso 回归模型
    lasso = Lasso(alpha=0.1)  # 可根据数据集调整 alpha 值

    # 拟合模型
    lasso.fit(X, Y)

    # 预测 tij 值
    t = np.round(lasso.predict(X)).astype(int)

    # 使用改进后的计数更新 BloomFilter
    #T = [0] * 18
    T = t

    arr_all_2 = [test_min(T, i) for i in range(num_interests)]

    # 输出改进后的兴趣数组
    for i, count in enumerate(arr_all_2):
        print(f"新兴趣{i+1}的个数为：{count}")

def create_design_matrix(c, m):
    X = np.zeros((len(c), m))

    for j in range(m):
        for i, tij in enumerate(c):
            X[i][j] = tij

    return X
