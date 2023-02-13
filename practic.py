# import requests
# from pprint import pprint
# api_url=f'https://api.ipify.org?format=json'
# res=requests.get(api_url)
# if res.status_code==200:
#     data=res.json()
#     ip=data.get('ip')
# api_location_url=f'https://ipapi.co/{ip}/json/'
# r=requests.get(api_location_url)
# if r.status_code==200:
#     ip_deatils=r.json()
#     Country_name=ip_deatils.get('country_name')
#     city=ip_deatils.get('city')
# sent=(Country_name,city)
# print(sent)
