import csv

def get_data(file_name,row_num):
    """从 CSV 文件中读取数据并返回二维数组"""
    item_counts = {}  # 字典用于统计元素出现次数
    with open(file_name, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过标题行
        for row in csv_reader:
            item_id = row[row_num]  
            if item_id in item_counts:
                item_counts[item_id] += 1
            else:
                item_counts[item_id] = 1
    data = [[item_id, count] for item_id, count in item_counts.items()]            
    return data

#print(get_data('test_data.csv',0))


