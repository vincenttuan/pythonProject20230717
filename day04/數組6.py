# 數組 電腦選號
# 樂透今彩539, 1~39 取出 5 個不會重複的數字
import random as r

# 創建一個 1~39 的數字列表
numbers = list(range(1, 40))
print(numbers)

# 創建一個 1~49 的數字列表
numbers2 = list(range(1, 50))
print(numbers2)

# 創建一個 0~9 的數字列表
numbers3 = list(range(0, 10))
print(numbers3)

# 從數字列表 numbers 中選擇 5 的不重複的數字
lotto = r.sample(numbers, 5)
print(lotto)

# 從數字列表 numbers2 中選擇 6 的不重複的數字
lotto2 = r.sample(numbers2, 6)
print(lotto2)

# 從數字列表 number3 中選擇 4 的可重複的數字
lotto3 = r.choices(numbers3, k=4)  # choices() 可以重複
print(lotto3)
