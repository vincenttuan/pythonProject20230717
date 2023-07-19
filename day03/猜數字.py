# 1~9 猜數字
# 若猜得比答案小 -> 顯示猜小了
# 若猜得比答案大 -> 顯示猜大了
# 若猜三次仍沒猜出來要顯示 "Sorry 次數已用完您沒猜對"
# 使用者所猜的數字範圍必須在 1~9 之間才有效才能進行答案比對
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
    # 請電腦猜
    pc_guess = random.randint(1, 9)
    print('電腦 1~9 請猜一個數字:%d' % pc_guess)
    # 比對答案
    if pc_guess > answer:
        print('電腦猜大了')
    elif pc_guess < answer:
        print('電腦猜小了')
    else:
        print('電腦答對了')
        break

    # 判斷是否 GG
    if count == 0:
        print("GG, Sorry 次數已用完您沒猜對")

print("遊戲結束")
