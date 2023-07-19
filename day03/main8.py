# 迴圈 while
# break 與 continue 的應用
# break 強制跳離迴圈
# continue 提早進行下一次的迴圈
count = 0
while count < 10:
    count = count + 1

    if count == 8:
        break
    elif count % 3 == 0:
        continue

    print(count)
