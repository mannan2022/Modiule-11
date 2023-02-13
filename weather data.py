from requests import get
from pprint import pprint
api_key='0d08dc2ccf4bb00a8558ea70c3bebc48'
City_name='Dhaka'
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={api_key}&units=metric'
# print(api_url)

res=get(api_url)
if res.status_code==200:
    data=res.json()
    country_name=data.get('sys').get('country')
    weather_data=data.get('main')
    feels_like=weather_data.get('feels_like')
    humidity=weather_data.get('humidity')
    pressure=weather_data.get('pressure')
    temp=weather_data.get('temp')
    print(feels_like,pressure,temp)
    # pprint(country_name)