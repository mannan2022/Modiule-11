# import requests
# from pprint import pprint
# api_key='33237522-2b80cf72e6b46d28d98bf3175'
# api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
# res=requests.get(api_url)
# api_data=res.json().get('hits')
# for url in api_data:
#     imaages_url=url.get('webformatURL')
#     file=open('img.txt','a+')
#     file.writelines(imaages_url+'\n')
#     file.close()
# file=open('img.txt','r+')
# url_list=file.readlines()
# file.close()
# new_url=[]
# for url in url_list:
#     kamal=url.strip('\n')
#     new_url.append(kamal)
#     print(new_url)
# singel_url=new_url[6]
# r=requests.get(singel_url)
# file=open('pixa.jpg','wb')
# file.write(r.content)
# file.close()
# from requests import get
# file=open('img.txt','r')
# url_list=file.readlines()
# file.close()
# i=0
# for url in url_list:
#     jaga=url.strip('\n')
#     r=get(url)
#     file=open(f'hasmir/{i}.jpg','wb')
#     file.write(r.content)
#     file.close()
#     i+=1
from requests import get
# from pprint import pprint
# api_key='33237522-2b80cf72e6b46d28d98bf3175'
# api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
# res=get(api_url)
# api_data=res.json().get('hits')
# for url in api_data:
#     imaages_url=url.get('webformatURL')
#     file=open('imag.txt','a+')
#     file.writelines(imaages_url+'\n')
#     file.close()
file=open('imag.txt','r+')
url_list=file.readlines()
file.close()
new_url=[]
for url in url_list:
    saiful=url.strip('\n')
    new_url.append(saiful)

singel_url=new_url[2]
r=get(singel_url)
file=open('pixa.jpg','wb')
file.write(r.content)
file.close()
