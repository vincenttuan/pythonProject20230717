# 自訂涵式
# return 有回傳值

def div(x, y):
    result = x / y
    return result

def mult(x, y):
    result = x * y
    return result

if __name__ == '__main__':
    result = div(123, 19)
    print("result =", result)
    print("result = %.2f" % result)

    result2 = mult(55, 13.7)
    print("result2 =", result2)
    print("result2 = %.2f" % result2)

