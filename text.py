import requests
url_list=[
    'https://www.dogfoodadvisor.com/best-dog-foods/best-dry-dog-foods/',
    'https://www.dogfoodadvisor.com/best-dog-foods/',
    'https://www.dogfoodadvisor.com/dog-food-reviews/brand/',

]
# for url in url_list:
#     res=requests.get(url)
#     text=f'{url}----{res.status_code}'
#     file=open('link status url.txt','r+')
#     url_list=file.readlines()
#     file.close()
#     print(url_list)
    
# text='this is simple text file'
# file=open('buying guide.txt','a+')
# file.writelines(text+'\n')
# file.close()
# text='Omayer Sagor is exceptional guy'
# file=open('sagor.txt','a+')
# file.writelines(text+'\n')
# file.close()
for url in url_list:
    r=requests.get(url)
    text=f'{url}---{r.status_code}'
    file=open('url.txt','r+')