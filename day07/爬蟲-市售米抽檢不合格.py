# 資料來源: 行政院農委會
# 資料網址: https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx
import json
import requests

url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
json_dict = json.loads(requests.get(url).text)
print("資料筆數", len(json_dict), json_dict)
rice_name = input('請輸入產品關鍵字:')
with open('bad_rice.txt', 'w', encoding='UTF-8') as file:
    index = 1
    for data in json_dict:
        if rice_name in data['品名']:
            print(index, data['品名'].strip(), data['不合格原因'].replace('\n', '').strip())
            #  請將這些資料儲存在 bad_rice.txt 文件中
            content = str(index) + '. ' + data['品名'].strip() + ' ' + data['不合格原因'].replace('\n', '').strip() + '\n'
            file.write(content)
            index += 1

print('寫檔完成 !')
