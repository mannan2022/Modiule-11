# import httpx
# from pprint import pprint
# city='Dhaka'
# api_key='0d08dc2ccf4bb00a8558ea70c3bebc48'
# api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# r=httpx.get(api_url)
# pprint(r.json())
import requests
# from pprint import pprint
url_list=[
    'The Best Dry Dog Food Brands 2023 | DogFoodAdvisor',
    'Best Dog Food Brands 2023 | DogFoodAdvisor',
    'Dog Food Advisor: Dog Food Reviews and Ratings',
]
for url in url_list:
    res=requests.get(url)
    print(res.status_code)
# file=open('url link.txt','w+')
# file.writelines(url_list)
# file.close()

# for url in url_list:
#     res=requests.get(url)
#     pprint(url,res.status_code,sep='--')
# text='This is template'
# file=open('buying.txt','a+')
# file.writelines(text+'\n')
# file.close()