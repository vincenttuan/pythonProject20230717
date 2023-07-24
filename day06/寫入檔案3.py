import re

new_salaries = [("Ada", 71000), ("Helen", 77000), ("Jo", 99999)]

with open('salary.txt', 'r', encoding='UTF-8') as file:
    # 使用 re 提取 name, salary 並直接轉 dict(字典)
    old_salaries = {name: int(salary) for name, salary in re.findall(r'(\w+)\s(\d+)', file.read())}

# 更新薪資或添加新的項目
print("更新前:", old_salaries)
old_salaries.update(new_salaries)
print("更新後:", old_salaries)

