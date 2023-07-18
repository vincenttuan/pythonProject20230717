# 隨機亂數
import random

num = random.randint(1, 10)  # 取出 1~10 之間的亂數
print(num)

# 樂透三星彩電腦選號
# 0~9 取出任意三個數字
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
print('電腦選號', n1, n2, n3)
print('電腦選號 %d %d %d' % (n1, n2, n3))
print('電腦選號 {0} {1} {2}'.format(n1, n2, n3))
