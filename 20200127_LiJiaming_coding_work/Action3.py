import numpy as np
import pandas as pd

'''step 1: 导出数据'''
data = pd.read_csv('car_complain.csv')
print(data)
#print(data.iloc[0])
#print(data.columns)
#print(data[0:600]
#print(data[0:600]['id'].values[0:600])
#print(data[0:600]['brand'].values[0:600])
#print(data[0:600]['problem'].values[0:600])

'''step 2：数据预处理'''

data = data.drop_duplicates()
print(data)

# 拆分问题状态数据列
data_problem_split = data['problem'].str.split(',', expand=True)

problem_count = data_problem_split
problem_count['Problem_Count'] = ''
for i in range(len(problem_count)):
    count = 0
    line = data_problem_split.iloc[i].isnull()
    for j in range(line.count() - 1):
        if not line[j]:
            count = count + 1
    problem_count['Problem_Count'][i] = count-1

# 拆分后的问题数目合并
data_concat = data.merge(data_problem_split, left_index=True, right_index=True, how='left')
#print(data_concat)

# 提取需要用到的列项目
data_problem = data_concat.loc[:, [ 'brand', 'car_model','Problem_Count']]

# 替换歧义名称
data_problem.replace({'一汽-大众':'一汽大众'},inplace=True)
data_problem.to_csv('data_problem.csv',index=False)

'''step 3: 数据统计'''
# 分别统计各品牌问题数目和投诉计次
problem_count_byBrand = data_problem.groupby('brand')['Problem_Count'].sum().sort_values(ascending=False)
print('各品牌问题总数')
print(problem_count_byBrand )
complain_count_byBrand = data_problem['Problem_Count'].groupby(data_problem['brand']).count().sort_values(ascending=False)
print('各品牌投诉总数')
print(complain_count_byBrand)

# 以车型为索引，分别统计问题数目和投诉计次
problem_count_byModel = data_problem.groupby('car_model')['Problem_Count'].sum().sort_values(ascending=False)
print('各车型问题总数')
print(problem_count_byModel)
complain_count_byModel = data_problem['Problem_Count'].groupby(data_problem['car_model']).count().sort_values(ascending=False)
print('各车型投诉总数')
print(complain_count_byModel)

# 获取各品牌车型数目
car_model_count = data_problem.drop_duplicates(subset=['brand','car_model'],keep='first')
print(car_model_count)

# 统计各品牌车型数目
model_count_sum = car_model_count['car_model'].groupby(car_model_count['brand']).count().sort_values(ascending=False)

print('各品牌车型数目:')
print(model_count_sum)
print()

Brand_problem_sum = data_problem.groupby('brand')['Problem_Count'].sum()
Brand_problem_count =  data_problem['Problem_Count'].groupby(data_problem['brand']).count()
car_model_count = car_model_count['car_model'].groupby(car_model_count['brand']).count()

print('品牌平均车型投诉数目排序：')
print(round(Brand_problem_count.divide(car_model_count).sort_values(ascending=False),2))
print('品牌平均车型问题数目排序：')
print(round(Brand_problem_sum.divide(car_model_count).sort_values(ascending=False),2))