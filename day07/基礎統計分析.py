import re
import statistics as stat
# 分析 salary.txt 中的相關統計資訊

# 將檔案內容轉化成 dict 資料格式
def get_from_file(file_name):
    file = open(file_name, 'r', encoding='UTF-8')
    # 將每一筆放到 dict 的結構中
    # {'John': 45000, 'Mary': 55000, 'Jack': 65000, 'Mole': 75000, 'Acer': 85000}
    # 利用正則表達式來表達
    result = {name: int(value) for name, value in re.findall(r'(\w+)\s(\d+)', file.read())}
    return result

if __name__ == '__main__':
    #result = get_from_file('salary.txt')
    result = get_from_file('age.txt')
    print(result)
    print(result.keys())  # 所有的 key
    print(result.values())  # 所有的 value

    salaries = result.values()
    print('總和: {:,}'.format(sum(salaries)))
    print('最高: {:,}'.format(max(salaries)))
    print('最低: {:,}'.format(min(salaries)))
    # 透過統計涵式來計算
    print('平均: {:,}'.format(stat.mean(salaries)))
    print('浮點平均: {:,}'.format(stat.fmean(salaries)))  # 浮點數快速平均
    print('中位數: {:,}'.format(stat.median(salaries)))
    print('標準差: {:,}'.format(stat.stdev(salaries)))
    print('變異係數: {:,}'.format(stat.stdev(salaries)/stat.mean(salaries)))










