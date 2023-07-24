import re

new_salaries = [("Ada", 71000), ("Helen", 77000), ("Jo", 99999)]

with open('salary.txt', 'r', encoding='UTF-8') as file:
    # 使用 re 提取 name, salary 並直接轉 dict(字典)
    old_salaries = {name: int(salary) for name, salary in re.findall(r'(\w+)\s(\d+)', file.read())}

# 更新薪資或添加新的項目
print("更新前:", old_salaries)
old_salaries.update(new_salaries)
print("更新後:", old_salaries)

# 將更新後的內容寫回到原始文件
# map 轉換, 將字典格式 {name, salary} 轉成字串 "name salary"
# lambda x, lambda 是一個涵式, x 指個是 old_salaries.items() 中的每一項
with open('salary.txt', 'w', encoding='UTF-8') as file:
    file.write('\n'.join(map(lambda x: f'{x[0]} {x[1]}', old_salaries.items())) + '\n')

print('寫入 OK')
