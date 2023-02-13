import requests
city_name='Dhaka'
api_key='b4b99243fb5f1a353fbfb53297c3e875'
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
res=requests.get(api_url)
print(res.status_code)