import requests
import datetime
# 資料來源: 台灣證券交易所
# https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={}&selectType=ALL

if __name__ == '__main__':
    date = datetime.datetime(2023, 7, 25)
    print(date)
    # 2023-07-25 00:00:00 轉 20230725
    date_str = date.strftime('%Y%m%d')  # 日期物件轉指定日期字串
    print(date_str)
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={}&selectType=ALL'
    url = url.format(date_str)
    print(url)
    # 抓取網頁資料
    data = requests.get(url).text
    # 統一去除雙引號 "
    data = data.replace('"', '')
    # 將 - 換成 -1
    data = data.replace('-', '-1')
    #print(data)
    # 發現若以 split(',') 來切割每一筆紀錄, 有用的欄位個數會是 8
    twii = []  # 用來放入有用的數組
    for row in data.split('\r\n'):  # windows 的換行 '\r\n', mac, linux 的換行 '\n'
        row = row.split(',')
        #print(len(row))
        if len(row) == 8:
            print(row)

