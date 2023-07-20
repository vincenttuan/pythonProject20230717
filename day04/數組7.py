# 數組 dict(字典格式), 每一組元素不可重複
# 元素 key:value (key 不可重複, value 可重複)
student1 = {'name': 'John', 'score': 95, 'age': 17, 'birth': '2006-7-20'}
print(student1)
print(student1['name'])
print(student1['score'])
# 加入性別
student1['sex'] = 'M'
print(student1)
# 加入分數 (若元素的 key 相同, 則原 value 會被取代)
student1['score'] = 100
print(student1)
# 刪除元素 'birth'
del student1['birth']
print(student1)
# 取出元素來使用, 取出後該元素就不會留在原始數組中
score = student1.pop('score')
print(score)
print(student1)

