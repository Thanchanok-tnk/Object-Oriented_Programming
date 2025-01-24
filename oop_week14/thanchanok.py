import requests

api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
symbol = 'AAPL'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
url_json = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=1min&apikey=YOUR_ALPHA_VANTAGE_API_KEY'

result = requests.get(url).json()

time_series = result['Time Series (1min)']
latest_time = list(time_series.keys())[0]
latest_data = time_series[latest_time]

open_price = latest_data['1. open']
high_price = latest_data['2. high']
low_price = latest_data['3. low']
close_price = latest_data['4. close']
volume = latest_data['5. volume']

print(f'สัญลักษณ์: {symbol}')
print(f'เวลา: {latest_time}')
print(f'ราคาเปิด: {open_price}')
print(f'ราคาสูงสุด: {high_price}')
print(f'ราคาต่ำสุด: {low_price}')
print(f'ราคาปิด: {close_price}')
print(f'ปริมาณการซื้อขาย: {volume}')