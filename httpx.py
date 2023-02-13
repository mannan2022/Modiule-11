import requests
from pprint import pprint
city='Dhaka'
api_key='0d08dc2ccf4bb00a8558ea70c3bebc48'
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

res=requests.get(api_url)
if res.status_code==200:
    pprint(res.json())