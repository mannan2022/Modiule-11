import requests
from pprint import pprint
ip_url='https://api.ipify.org?format=json'
r=requests.get(ip_url)
if res.status_code==200:
    data=r.json()
    ip=data.get('ip')
api_location_url=f'https://ipapi.co/{ip}/json/'
res=requests.get(api_location_url)
if res.status_code==200:
    location_details=res.json()
    