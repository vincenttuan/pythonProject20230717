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
            # 證券代號 證券名稱 殖利率 股利年度 本益比 股價淨值比 財報
            try:
                stock = {}
                stock.setdefault('證券代號', row[0])
                stock.setdefault('證券名稱', row[1])
                stock.setdefault('殖利率', float(row[2]))
                stock.setdefault('股利年度', row[3])
                stock.setdefault('本益比', float(row[4]))
                stock.setdefault('股價淨值比', float(row[5]))
                stock.setdefault('財報', row[6])
                # 將 stock 加入到 twii
                twii.append(stock)
            except ValueError:
                pass
        print(twii)

