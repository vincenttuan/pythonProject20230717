# 邏輯判斷 if-else, if-elif-else
# 使用者輸入一個整數如何判斷是奇數或偶數
# 例如: 輸入 12 印出 偶數
#      輸入 15 印出 奇數
# 提示: 利用 % 餘數與 == 來進行判斷
try:
    x = int(input('請輸入一個整數:'))
    if x % 2 == 0:
        print("%d 是偶數" % x)
    else:
        print("%d 是奇數" % x)
except:
    print('資料輸入錯誤')
