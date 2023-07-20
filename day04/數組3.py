# 數組 撲克牌與亂數
import random as r

poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
print(poker)
print(len(poker))
# 利用亂數洗牌
r.shuffle(poker)
print(poker)

