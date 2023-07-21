# 自訂函數
# 我可以放任意的參數數量
# get_sum(10, 20), get_sum(10, 20, 30), get_sum(10, 20, 30, 40)
def get_sum(*num):
    return sum(num)


def fun(**kwargs):  # ** 支援字典格式 (kwargs = keyword arguments)
    for key, vale in kwargs.items():
        print(key, vale)

if __name__ == '__main__':
    print(get_sum())
    print(get_sum(10, 20))
    print(get_sum(10, 20, 30, 40, 50))

    fun(a=4, b=5)
    fun(score=100, height=170, weight=60)

