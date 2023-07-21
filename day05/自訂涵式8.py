# 自訂涵式-數組
# 請設計一個方法可以計算數組的總分,平均與標準差(判斷數組的集中度)
# array 代表的是數組參數
# API 設計如下:
# get_sum(array), get_average(array), get_sd(array)
import statistics

def get_sum(array):
    return sum(array)


def get_average(array):
    return statistics.mean(array)  # mean 算術平均數


def get_sd(array):
    return statistics.stdev(array, xbar=None)  # xbar(可選) 預先計算的平均數


def get_cv(array):  # 變異係數
    sd = get_sd(array)
    avg = get_average(array)
    cv = sd / avg
    return cv

if __name__ == '__main__':
    a = [100, 70, 90, 80]
    b = [10, 15, 18, 13]
    print(get_sum(a), get_average(a), get_sd(a))
    print(get_sum(b), get_average(b), get_sd(b))

    h = [170.0, 150.5, 160]  # 身高(cm)
    w = [70, 60, 65]  # 體重(kg)
    print(get_cv(h), get_cv(w))






