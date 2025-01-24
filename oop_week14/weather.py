import requests

api_key = '4b9fb2bb3210fa0f92c4f10afc0730a4'
city = 'Bangkok'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
url_json = 'https://api.openweathermap.org/data/2.5/weather?q=Bangkok&appid=4b9fb2bb3210fa0f92c4f10afc0730a4'

result = requests.get(url).json()
#print(result)

city = result['name']
country = result['sys']['country']
weather = result['weather'][0]['main']
description = result['weather'][0]['description']
temp = result['main']['temp'] - 273.15

print(f'เมือง {city} ประเทศ {country}')
print(f'สภาพอากาศวันนี้ {weather} ลักษณะ {description}')
print(f'อุณหภูมิตอนนี้ {temp:.2f} c ')