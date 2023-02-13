import requests
url=[
    'https://www.greatpetcare.com/cat-food/best-cat-food/',
    'https://www.thesprucepets.com/best-premium-dry-cat-food-4150202',
    'https://nymag.com/strategist/article/best-cat-food.html',
]
for kamal in url:
    r=requests.get(kamal)
    text=f'{kamal}----{r.status_code}'
    file=open('link check.txt','a+')
    file.writelines(text+ '\n')
    file.close()
    file=open('link check.txt','r+')
    url_list=file.readlines()
    file.close()
    print(url_list)

# for link in url:
#     r=requests.get(link)
#     text=f'{link}---{r.status_code}'
#     file=open('link status.txt','a+')
#     file.writelines(text+'\n')
#     file.close()
#     file=open('link status.txt','r+')
#     url_list=file.readlines()
#     file.close()
#     print(url_list)
# text='kamal bhaier line ekhon direct'
# file=open('kamal.txt','a+')
# file.writelines(text+ '\n')
# file.close()
# kamal='hoga mara khaiya boisa ache'
# file=open('text file.txt','a+')
# file.writelines(kamal+ '\n')
# file.close()