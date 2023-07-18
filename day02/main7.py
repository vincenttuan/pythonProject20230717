# 字串分析
words = "she sell sea shell on the sea shore"
print(words, len(words))  # len() 得到字串長度
print(words[2:10])  # 抓2(含)~10(不含)位置的資料
print('有幾個 s : %d' % words.count('s'))
print('有幾個 sea : %d' % words.count('sea'))
print('請問 shell 的位置: %d' % words.find('shell'))
print('請問 she 的位置: %d' % words.find('she'))
print('請問 sky 的位置: %d' % words.find('sky'))
# 透過 ' ' 來切割字串 split(' ')
# 可以得出 words 有幾個單字詞
array = words.split(' ')
print(array, len(array))
print(array[3])

