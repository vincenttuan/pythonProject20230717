# 人機互動(使用者輸入並計算)
chinese = input('請輸入國文成績:')
print('國文成績是', chinese)
print('國文成績是 %s' % chinese)
print('國文成績是 {0}'.format(chinese))
english = input('請輸入英文成績:')
print('英文成績是', english)
print('英文成績是 %s' % english)
print('英文成績是 {0}'.format(english))
# 計算總分 = ?
print(chinese + english)
print(int(chinese) + int(english))  # 利用 int() 將字串轉成整數

