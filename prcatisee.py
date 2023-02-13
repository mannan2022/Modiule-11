import requests
from pprint import pprint
api_key='33237522-2b80cf72e6b46d28d98bf3175'
api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
res=requests.get(api_url)
api_data=res.json().get('hits')
for url_list in api_data:
    image_url=url_list.get('webformatURL')
    file=open('sagor.txt','a+')
    file.writelines(image_url+'\n')
    file.close()
    file=open('sagor.txt','r+')
    url_list=file.readlines()
    file.close()
    new=[]
    for url in url_list:
        hasmir=url.strip('\n')
        new.append(hasmir)
singel=new[0]
r=requests.get(singel)
file=open('pixa.jpg','wb')
file.write(r.content)
file.close()
