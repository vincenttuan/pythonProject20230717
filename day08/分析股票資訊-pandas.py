import pandas as pd

# 讀取本地的 CSV 檔
data = pd.read_csv('BWIBBU_d_ALL_20230725_utf8.csv', header=1, encoding='utf-8')

# 列印 DataFrame 的欄位名稱
print(data.columns)

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
