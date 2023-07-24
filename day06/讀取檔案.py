# 讀取: person.txt 的內容
# 目的: 計算平均年齡
file = open('person.txt', 'r', encoding='UTF-8')
# 讀取整個檔案內容到數組中
rows = file.readlines()
print("資料筆數:", len(rows))
# strip() 除去字串後面的換行符號與空白
print("第 1 筆:", rows[0].strip())
print("第 2 筆:", rows[1].strip())
print("最末筆:", rows[len(rows)-1].strip())

total = 0
for data in rows:
    array = data.strip().split(" ")
    name = array[0]
    age = array[1]
    print('name:', name, ' age:', age)
    total = total + int(age)
print('total:', total)
average = total / len(rows)
print('average:', average)

