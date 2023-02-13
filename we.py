import requests
City_name='Dhaka'
Country_code='+880'
Api_key='0d08dc2ccf4bb00a8558ea70c3bebc48'
api_url=f'https://pro.openweathermap.org/data/2.5/forecast/hourly?q={City_name},{Country_code}&appid={Api_key}'

r=requests.get(api_url)
print(r.json())