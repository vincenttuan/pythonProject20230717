# 繪出薪資折線圖
import re
import matplotlib.pyplot as plt

# 讀取檔案內容
pattern = re.compile(r'(\w+)\s(\d+)')
with open('salary.txt', 'r', encoding='UTF-8') as file:
    salaries = {name: int(salary) for name, salary in pattern.findall(file.read())}

print(salaries)
# 提取名字(names)與薪資(values)
names = salaries.keys()
values = [salaries[name] for name in names]
print(names)
print(values)

# 繪製折線圖
plt.plot(names, values, marker='o')
plt.title('Salaries')
plt.show()





