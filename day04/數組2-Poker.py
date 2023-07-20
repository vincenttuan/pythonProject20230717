# 數組 撲克牌
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(poker)
print(len(poker))
# 洗牌(換位置)
poker[0], poker[1] = poker[1], poker[0]
print(poker)


