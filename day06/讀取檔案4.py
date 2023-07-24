import re
# 讀取: salary.txt 的內容
# 目的: 計算總薪資, 平均薪資, 最高薪資, 最低薪資
with open('salary.txt', 'r', encoding='UTF-8') as file:
    content = file.read()

pattern = re.compile(r'(\w+)\s(\d+)')
matches = pattern.findall(content)

# 將所有的 salary 儲存到一個列表 salaries 中
salaries = [int(salary) for name, salary in matches]
print(salaries)



# 計算總薪資, 平均薪資, 最高薪資, 最低薪資

