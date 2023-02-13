import requests
urls_list=[
    'https://www.dogfoodadvisor.com/best-dog-foods/best-dry-dog-foods/',
    'https://www.dogfoodadvisor.com/',
    'https://www.dogfoodadvisor.com/best-dog-foods/best-puppy-foods/',
]
for url in urls_list:
    res=requests.get(url)
    text=f'{url}-----{res.status_code}'
    # file=open('link status url.txt','a+')
    # file.writelines(text+'\n')
    # file.close()
    file=open('link status url.txt','r+')
    urls_list= file.readlines()

    file.close()
    print(urls_list)

# text='This is simple text 3'
# file=open('best_cooker.txt','a+')
# file.writelines(text+ '\n')
# file.close()