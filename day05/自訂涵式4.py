# 自訂涵式
# return 有回傳值

def div(x, y):
    result = x / y
    return result


if __name__ == '__main__':
    result = div(123, 19)
    print("result =", result)
    print("result = %.2f" % result)
