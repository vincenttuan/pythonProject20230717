# 數組 電腦選號
# 樂透今彩539, 1~39 取出 5 個不會重複的數字
import random as r

# 創建一個 1~39 的數字列表
numbers = list(range(1, 40))
print(numbers)

# 創建一個 1~49 的數字列表
numbers2 = list(range(1, 50))
print(numbers2)


# 從數字列表中選擇 5 的不重複的數字
lotto = r.sample(numbers, 5)
print(lotto)

lotto2 = r.sample(numbers2, 6)
print(lotto2)
