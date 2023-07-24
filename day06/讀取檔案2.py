import re
# 讀取: person.txt 的內容
# 目的: 計算平均年齡
# 讀取檔案內容
with open('person.txt', 'r', encoding='UTF-8') as file:
    content = file.read()

print(content, type(content))
# 使用一個正則表示式來匹配買一行, 並提取name與age
# \w: 任何字母,數字或_
# \s: 任何空白或換行符號
# \d: 任何數字
# +: 一次或多次
pattern = re.compile(r'(\w+)\s(\d+)')
matches = pattern.findall(content)
print(matches)

