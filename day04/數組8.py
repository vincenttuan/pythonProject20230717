# 數組 dict 的應用
emp1 = {'name': 'John', 'salary': 60000}
emp2 = {'name': 'Mary', 'salary': 50000}
emp3 = {'name': 'Jack', 'salary': 80000}
emp4 = {'name': 'Rose', 'salary': 70000}
# 請問總薪資為何 ?
employees = [emp1, emp2, emp3, emp4]
print(employees)
# 使用 for-in + sum() 來計算
total_salary = sum(emp['salary'] for emp in employees)
print(total_salary)
# 請問誰(name)的薪資最高 ?
highest_salary = 0
highest_name = None
# 透過替換法
for emp in employees:  # 輪詢每一個員工
    if emp['salary'] > highest_salary:
        highest_salary = emp['salary']
        highest_name = emp['name']

print(highest_name, highest_salary)
