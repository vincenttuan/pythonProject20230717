# 天氣資料查詢
# 網路位置: https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}
city_name = 'taipei,TW'
key = '2e7c38444416f91b223a919462124db4'  # 請用自己的 key
url = 'https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}'
url = url.format(city_name, key)
print(url)



