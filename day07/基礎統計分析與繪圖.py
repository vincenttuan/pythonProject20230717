# 比較 salary 與 age 哪一個分散程度大(集中度小)?
from day07.基礎統計分析 import get_from_file
import statistics as stat
import matplotlib.pyplot as plt

# 計算並取得變異係數
def get_cv(values):
    sd = stat.stdev(values)
    avg = stat.mean(values)
    cv = sd / avg
    return cv


if __name__ == '__main__':
    salaries = get_from_file('salary.txt')
    ages = get_from_file('age.txt')

    salaries_cv = get_cv(salaries.values())
    ages_cv = get_cv(ages.values())

    print(salaries, 'cv =', salaries_cv)
    print(ages, 'cv =', ages_cv)

    print("{} 的分散程度大".format('salary' if salaries_cv > ages_cv else 'age'))

    # 繪製統計圖表
    all_salaries = salaries.values()
    all_ages = ages.values()
    all_names = ages.keys()
    print(all_salaries, all_ages, all_names)

    plt.plot(all_names, all_salaries)
    plt.plot(all_names, all_ages)

    plt.show()
