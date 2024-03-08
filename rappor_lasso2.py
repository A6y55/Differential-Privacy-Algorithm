import random
import math
import numpy as np
from sklearn.linear_model import Lasso

class BloomFilter:
    def __init__(self):
        self.arr = [0] * 18

    def hash1(self, num):
        hash_value = 0
        if num == 0:
            return 0
        while True:
            if num > 0:
                k = num % 10
                hash_value = hash_value * 1311 + k
                num = num // 10
            else:
                return hash_value

    def hash2(self, num):
        hash_value = 0
        if num == 0:
            return 0
        while True:
            if num > 0:
                k = num % 10
                hash_value = hash_value * 3677 + k
                num = num // 10
            else:
                return hash_value

    def hash3(self, num):
        hash_value = 0
        if num == 0:
            return 0
        while True:
            if num > 0:
                k = num % 10
                hash_value = hash_value * 4423 + k
                num = num // 10
            else:
                return hash_value

    def hash4(self, num):
        hash_value = 0
        if num == 0:
            return 0
        while True:
            if num > 0:
                k = num % 10
                hash_value = hash_value * 4871 + k
                num = num // 10
            else:
                return hash_value

    def in_4_hash(self, num):
        self.arr[self.hash1(num) % 18] = 1
        self.arr[self.hash2(num) % 18] = 1
        self.arr[self.hash3(num) % 18] = 1
        self.arr[self.hash4(num) % 18] = 1

    def test(self, num):
        if self.arr[self.hash1(num) % 18] != 1:
            return False
        if self.arr[self.hash2(num) % 18] != 1:
            return False
        if self.arr[self.hash3(num) % 18] != 1:
            return False
        if self.arr[self.hash4(num) % 18] != 1:
            return False
        return True

    def answer(self):
        result = []
        for i in range(100):
            if self.test(i):
                result.append(i)
        return result

    def hash11(self, num):
        temp = [0] * 4
        num = num * num
        if num < 26:
            return num + 2
        for i in range(4):
            k = num % 10
            temp[i] = k
            num = num // 23
        return temp[2] * 10 + temp[1]

    def hash12(self, num):
        temp = [0] * 4
        num = num * num
        if num < 26:
            return num + 1
        for i in range(4):
            k = num % 10
            temp[i] = k
            num = num // 11
        return temp[2] * 10 + temp[1]

    def hash13(self, num):
        temp = [0] * 4
        num = num * num
        if num < 26:
            return num + 5
        for i in range(4):
            k = num % 10
            temp[i] = k
            num = num // 13
        return temp[2] * 10 + temp[1]

    def hash14(self, num):
        temp = [0] * 4
        num = num * num
        if num < 26:
            return num + 9
        for i in range(4):
            k = num % 10
            temp[i] = k
            num = num // 17
        return temp[2] * 10 + temp[1]

    def in_4_hash1(self, num):
        self.arr[self.hash11(num) % 18] = 1
        self.arr[self.hash12(num) % 18] = 1
        self.arr[self.hash13(num) % 18] = 1
        self.arr[self.hash14(num) % 18] = 1

    def test0(self, num):
        if self.arr[self.hash11(num) % 18] != 1:
            return False
        if self.arr[self.hash12(num) % 18] != 1:
            return False
        if self.arr[self.hash13(num) % 18] != 1:
            return False
        if self.arr[self.hash14(num) % 18] != 1:
            return False
        return True

    def test01(self, num):
        if self.arr[self.hash11(num) % 18] <= 0:
            return 0
        min_val = self.arr[self.hash11(num) % 18]

        if self.arr[self.hash12(num) % 18] <= 0:
            return 0
        min_val = min(min_val, self.arr[self.hash12(num) % 18])

        if self.arr[self.hash13(num) % 18] <= 0:
            return 0
        min_val = min(min_val, self.arr[self.hash13(num) % 18])

        if self.arr[self.hash14(num) % 18] <= 0:
            return 0
        min_val = min(min_val, self.arr[self.hash14(num) % 18])

        return min_val

def random_permanent(f):
    a = random.randint(0, 9999)
    F = int(f * 10000)
    if a < F // 2:
        return 1
    if a > F:
        return -1
    return 0

def random_instant(p, q, a):
    s = random.randint(0, 9999)
    if a == 1:
        return 1 if s < q * 10000 else 0
    if a == 0:
        return 1 if s < p * 10000 else 0

def test(f, p, q, num1, num2, c, arr_all):  # 将 c 和 arr_all 作为参数传递
    A = BloomFilter()
    A.in_4_hash1(num1)
    A.in_4_hash1(num2)

    for k in range(18):
        s = random_permanent(f)
        if s == 0:
            A.arr[k] = 0
        if s == 1:
            A.arr[k] = 1

    s = [0] * 18
    for k in range(18):
        if A.arr[k] == 0:
            s[k] = random_instant(p, q, A.arr[k])
            A.arr[k] = s[k]

    for k in range(18):
        if A.arr[k] == 1:
            c[k] += 1

    arr_all[num1] += 1
    arr_all[num2] += 1

def calculate_epsilon(f):
    return -math.log(1/f - 1)

def improved_counting():
    N = 10000  
    random.seed()

    num_interests = 100
    epsilon = float(input("请输入扰动的参数: "))  # 输入扰动的参数 epsilon
    f = 1.0 / (1.0 + math.exp(epsilon))

    p = float(input("请输入p: "))  # 输入p
    q = float(input("请输入q: "))  # 输入q

    c = [0] * 18  # 初始化 c 列表
    arr_all = [0] * num_interests  # 初始化 arr_all 列表

    for i in range(5000):
        test(f, p, q, 10, 11, c, arr_all)
    for i in range(1000):
        test(f, p, q, 12, 13, c, arr_all)
    for i in range(4000):
        test(f, p, q, 14, 15, c, arr_all)

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
    T = BloomFilter()
    T.arr = t

    arr_all_2 = [T.test01(i) for i in range(num_interests)]

    # 输出改进后的兴趣数组
    for i, count in enumerate(arr_all_2):
        print(f"新兴趣{i+1}的个数为：{count}")

def create_design_matrix(c, m):
    X = np.zeros((len(c), m))

    for j in range(m):
        for i, tij in enumerate(c):
            X[i][j] = tij

    return X

if __name__ == "__main__":
    improved_counting()