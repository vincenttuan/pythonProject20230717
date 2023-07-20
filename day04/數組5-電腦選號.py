# 數組 電腦選號
# 樂透今彩539, 1~39 取出 5 個不會重複的數字
import random as r

lotto = set()
while len(lotto) < 5:
    num = r.randint(1, 39)  # 取得 1~39 的隨機數
    print('num =', num)
    lotto.add(num)

print(lotto)
