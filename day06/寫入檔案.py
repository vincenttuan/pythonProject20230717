salaries = [("Rose", 38000), ("Helen", 77000), ("Jo", 56000)]

# 開啟 salaries.txt 文件並寫入資料
# w: 完整寫入(不保留原來的資料), a: append 加入(保留原來的資料)
with open('salary.txt', 'a', encoding='UTF-8') as file:
    for name, salary in salaries:
        # format 標準版
        # file.write("{} {}\n".format(name, salary))
        # format 簡化版
        file.write(f"{name} {salary}\n")
print('寫入 OK')

