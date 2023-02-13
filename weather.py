# from requests import get
# from pprint import pprint
# city='Dhaka'
# api_key='0d08dc2ccf4bb00a8558ea70c3bebc48'
# api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# res=get(api_url)
# if res.status_code==200:
#     data=res.json()
#     Country_name=data.get('sys').get('country')
#     weather_data=data.get('main')
#     feels_like=weather_data.get('feels_like')
#     humidity=weather_data.get('humidity')
#     pressure=weather_data.get('pressure')
#     temp=weather_data.get('temp')
#     temp_max=weather_data.get('temp_max')
#     temp_min=weather_data.get('temp_min')
# sentence=(Country_name,'Feels like',feels_like,'humidity',humidity,pressure,'temp',temp,temp_max,temp_min)
# pprint(sentence)
import requests
api_key=''

 