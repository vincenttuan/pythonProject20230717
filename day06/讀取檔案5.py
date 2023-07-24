import re

pattern = re.compile(r'(\w+)\s(\d+)')

with open('salary.txt', 'r', encoding='UTF-8') as file:
    salaries = [int(salary) for name, salary in pattern.findall(file.read())]

print('資料筆數:{}\n總薪資:{}\n平均薪資:{:.1f}\n最高薪資:{}\n最低薪資:{}'
      .format(len(salaries), sum(salaries), sum(salaries)/len(salaries), max(salaries), min(salaries)))
