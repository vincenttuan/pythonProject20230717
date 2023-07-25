# 比較 salary 與 age 哪一個分散程度大(集中度小)?
from day07.基礎統計分析 import get_from_file
import statistics as stat

# 計算並取得變異係數
def get_cv(values):
    sd = stat.stdev(values)
    avg = stat.mean(values)
    cv = sd / avg
    return cv


if __name__ == '__main__':
    salaries = get_from_file('salary.txt')
    ages = get_from_file('age.txt')
    print(salaries, 'cv =', get_cv(salaries.values()))
    print(ages, 'cv =', get_cv(ages.values()))

