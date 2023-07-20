# 數組:
# []     -> 稱為 List/陣列, 資料元素可重複
# set()  -> 稱為 Set, 資料元素不會重複
# dict() -> 稱為字典格式/map, 資料(key/value的形式) key 不可重複, value 可重複
a = [1, 3, 5, 7, 5]
print(a)
a[0] = 2  # 變更元素內容
print(a)
a.append(9)  # 增加元素內容
print(a)
a.remove(5)  # 移除元素(5是指元素的內容)
print(a)
a.__delitem__(2)  # 移除元素(2是指元素的位置)
print(a)
a.reverse()  # 資料反轉
print(a)
a.sort()  # 資料排序(小->大), 自然排序
print(a)
print('max:', max(a))  # 取得最大值
print('min:', min(a))  # 取得最小值
