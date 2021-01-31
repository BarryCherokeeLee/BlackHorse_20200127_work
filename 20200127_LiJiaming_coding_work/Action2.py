import numpy as np

person_info_type = np.dtype({
    'names': ['name', 'chinese', 'english', 'math'],
    'formats': ['S32', 'i', 'i', 'i']})

person_info = np.array(
    [
        ('Zhang Fei', 68, 65, 30),
        ('Guan Yu', 95, 76, 98),
        ('Liu Lei', 98, 86, 88),
        ('Dian Wei', 90, 88, 77),
        ('Xu Chu', 80, 90, 90)
    ], dtype=person_info_type)

name = person_info[:]['name']
chinese = person_info[:]['chinese']
english =person_info[:]['english']
math = person_info[:]['math']
sum_score = chinese+english+math



print("********平均成绩********")
print("语文平均成绩：", np.mean(chinese))
print("英语平均成绩：", np.mean(english))
print("数学平均成绩：", np.mean(math))
print("********最高与最低成绩********")
print("最高语文成绩：", np.max(chinese))
print("最低语文成绩：", np.min(chinese))
print("最高英语成绩：", np.max(english))
print("最低英语成绩：", np.min(english))
print("最高数学成绩：", np.max(math))
print("最低数学成绩：", np.min(math))
print("********成绩方差********")
print("语文成绩方差：", np.var(chinese))
print("英语成绩方差：", np.var(english))
print("数学成绩方差：", np.var(math))
print("********成绩标准差********")
print("语文成绩标准差：", np.std(chinese))
print("英语成绩标准差：", np.std(english))
print("数学成绩标准差：", np.std(math))
print("********总成绩排名********")
print(np.sort(sum_score))

