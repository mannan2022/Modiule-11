# import requests
# from pprint import pprint
# api_key='33237522-2b80cf72e6b46d28d98bf3175'
# api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
# res=requests.get(api_url)
from requests import get
from pprint import pprint
api_key='33237522-2b80cf72e6b46d28d98bf3175'
api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
res=get(api_url)
api_data=res.json().get('hits')
for url in api_data:
    images_url=url.get('webformatURL')
    file=open('text.txt','a+')
    file.writelines(images_url+'\n')
    file.close