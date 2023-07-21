# 請設計一個 get_bmi(h, w) 的自訂涵式
# 主程式可以透過調用該方法得到 bmi 的值
def get_bmi(h, w):  # 取得 bmi 的值
    bmi = w / (h/100)**2
    return bmi

def get_bmi_result(bmi):  # 診斷 bmi 的結果
    if bmi <= 18:
        return "過輕"
    elif bmi > 23:
        return "過重"
    return "正常"

def get_bmi_and_result(h, w):
    bmi = get_bmi(h, w)
    result = get_bmi_result(bmi)
    return bmi, result

if __name__ == '__main__':
    h = float(input('請輸入身高cm:'))
    w = float(input('請輸入體重kg:'))
    bmi, result = get_bmi_and_result(h, w)
    print(bmi, result)

