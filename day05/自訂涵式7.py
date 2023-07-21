# 調用自己在其他 .py 上所設計的涵式
from day05.自訂涵式6 import get_bmi, get_bmi_result, get_bmi_and_result

if __name__ == '__main__':
    h = 170
    w = 60
    bmi, result = get_bmi_and_result(h, w)
    print(bmi, result)

    bmi2 = get_bmi(180, 80)
    result2 = get_bmi_result(bmi2)
    print(bmi2, result2)

