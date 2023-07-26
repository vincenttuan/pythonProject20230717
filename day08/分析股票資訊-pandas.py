import io
import pandas as pd
import datetime
import requests

# 讀取本地的 CSV 檔
# data = pd.read_csv('BWIBBU_d_ALL_20230725_utf8.csv', header=1, encoding='utf-8')

# 讀取雲端資料
date = datetime.datetime(2023, 7, 25)
date_str = date.strftime('%Y%m%d')
url = f'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={date_str}&selectType=ALL'
# 透過 requests 取雲端資料, 解決 SSL 簽證問題
response = requests.get(url)
data_io = io.StringIO(response.text)  # 類似一個檔案, 只是該檔案在記憶體

data = pd.read_csv(data_io, header=1, encoding='utf-8')

#----------------------------------------------------------------------------------
# 列印 DataFrame 的欄位名稱
#print(data.columns)

# 將 '-' 換成 NaN
data.replace('-', float('NaN'), inplace=True)

# 將適當的列轉為數字
for col in ['殖利率(%)', '本益比', '股價淨值比']:
    data[col] = pd.to_numeric(data[col], errors='coerce')  # 使用 'coerce' 參數將轉換過程中的錯誤值設為 NaN

# 買一檔股票的條件
condition = (data['本益比'] > 0) & (data['本益比'] <= 12) & \
            (data['殖利率(%)'] >= 7) & \
            (data['股價淨值比'] > 0) & (data['股價淨值比'] <= 1)

# 使用條件過濾數據並打印結果
print(data[condition])

# 只想印出證券代號
symbols = data.loc[condition, '證券代號'].tolist()
print(symbols)

# 只想印出證券名稱
names = data.loc[condition, '證券名稱'].tolist()
print(names)

# 透過 LineNotify 通知客戶
token = 'Qk9xIdAgvAyivGGqneRRWtuHgTAu16dbkMNxCkAGAUr'
url = 'https://notify-api.line.me/api/notify'
headers = {
    "Authorization": "Bearer " + token
}
# 輸入要傳送的內容
# msg = "颱風來了~~ "
# msg = symbols + names
msg = "最新颱風動態 https://www.youtube.com/watch?v=EqfBQiODfu8"
package_id = '6136'
stick_id = '10551377'

payload = {
    "message": msg,
    "stickerPackageId": package_id,
    "stickerId": stick_id
}
# 傳送到 LineNotify
# result 可以得到回應結果, 若看到 200 表示 OK
result = requests.post(url, headers=headers, params=payload)
print('LineNotify result:', result)
