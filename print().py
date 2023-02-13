import requests
from pprint import pprint
api_key='0d08dc2ccf4bb00a8558ea70c3bebc48'
City_name='Dhaka'
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={api_key}&units=metric'
response=requests.get(api_url)
if response.status_code==200:
    data=response.json()
    city=data.get('name')
    weather_data=data.get('main')
    feels_like=weather_data.get('feels_like')
    temp=weather_data.get('temp')
    temp_max=weather_data.get('temp_max')
    temp_min=weather_data.get('temp_min')
sentence=(city,feels_like,temp,temp_max,temp_min)
pprint(sentence)