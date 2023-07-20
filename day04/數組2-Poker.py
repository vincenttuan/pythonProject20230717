# 數組 撲克牌
import random as r

poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(poker)
print(len(poker))
# 洗牌(換位置)
poker[0], poker[1] = poker[1], poker[0]
print(poker)
# 亂數洗牌(隨機換位置) 洗一次
pos1 = r.randint(0, 12)
pos2 = r.randint(0, 12)
poker[pos1], poker[pos2] = poker[pos2], poker[pos1]
print(poker)
# 亂數洗牌(隨機換位置) 洗100次
for i in range(0, 100):  # i = 0 .. 99
    pos1 = r.randint(0, 12)
    pos2 = r.randint(0, 12)
    poker[pos1], poker[pos2] = poker[pos2], poker[pos1]
print(poker)
