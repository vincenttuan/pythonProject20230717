# 自訂涵式 return 多組資料
# 同時計算乘與除的結果

def multi(x, y):
    result = x * y
    return result

def div(x, y):
    result = x / y
    return result

def multi_and_div(x, y):
    multi_result = multi(x, y)  # 相乘的結果
    div_result = div(x, y)    # 相除的結果
    return multi_result, div_result  # 同時回傳二個結果


if __name__ == '__main__':
    res1, res2 = multi_and_div(20, 5)
    print(res1, res2)

    res3 = multi(20, 5)
    print(res3)

    res4 = div(20, 5)
    print(res4)

