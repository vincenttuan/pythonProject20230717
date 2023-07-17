# 今有雞、兔同籠，上有三十五頭，下九十四足。問雉、兔各幾何？
'''
算式
假設都是雞會有幾隻腳
35 * 2 = 70
94 - 70 = 24/(4-2) = 12 ... 兔子
35 - 12 = 23 ... 雞
'''

total = 35
feet = 94

rabbit = (feet - total*2) / (4-2)
chicken = total - rabbit

print('雞 %d, 兔 %d' % (chicken, rabbit))
