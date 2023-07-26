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


