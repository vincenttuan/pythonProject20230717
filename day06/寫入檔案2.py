import re
new_salaries = [
    ('Mary', 55000), ('Happy', 88000), ('John', 52000)
]

with open('salary.txt', 'r', encoding='UTF-8') as file:
    content = file.read()

# 提取名字與薪資
pattern = re.compile(r'(\w+)\s(\d+)')
# {'John': 45000, 'Mary': 55000, ...}
old_salaries = {name: int(salary) for name, salary in pattern.findall(content)}
print(old_salaries)

# 利用 dict 的特性同名更新薪資或添加新項目
for name, salary in new_salaries:
    old_salaries[name] = salary
print(old_salaries)

# 回寫到 salary.txt 文件
with open('salary.txt', 'w', encoding='UTF-8') as file:
    for name, salary in old_salaries.items():
        file.write(f"{name} {salary}\n")

print('寫檔 OK')

