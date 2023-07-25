import json
import requests
# 天氣資料查詢
# 網路位置: https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}
city_name = 'taipei,TW'
key = '2e7c38444416f91b223a919462124db4'  # 請用自己的 key
url = 'https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}'
url = url.format(city_name, key)
print(url)

json_dict = json.loads(requests.get(url).text)
print(json_dict, type(json_dict))
print('天氣狀況', json_dict['weather'][0]['main'])
print('天氣說明', json_dict['weather'][0]['description'])
print('現在氣溫 ', float(json_dict['main']['temp'])-273.15)
print('體感溫度 ', float(json_dict['main']['feels_like'])-273.15)
print('現在濕度 ', json_dict['main']['humidity'])
print('現在風速 ', json_dict['wind']['speed'])
print('雲層覆蓋 ', json_dict['clouds']['all'])
