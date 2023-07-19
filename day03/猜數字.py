# 1~9 猜數字
# 若猜得比答案小 -> 顯示猜小了
# 若猜得比答案大 -> 顯示猜大了
# 若猜三次仍沒猜出來要顯示 GG
import random
answer = random.randint(1, 9)
count = 3
#print('answer =', answer)
while count > 0:
    # 請玩家猜
    user_guess = int(input('玩家 1~9 請猜一個數字:'))
    # count 扣掉一次
    count = count - 1
    # 比對答案
    if user_guess > answer:
        print('玩家猜大了')
    elif user_guess < answer:
        print('玩家猜小了')
    else:
        print('玩家答對了')
        break


