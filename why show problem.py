import httpx
from pprint import pprint
url_list=[
    'The Best Dry Dog Food Brands 2023 | DogFoodAdvisor',
    'Best Dog Food Brands 2023 | DogFoodAdvisor',
    'Dog Food Advisor: Dog Food Reviews and Ratings',
]
for url in url_list:
    res=httpx.get(url)
    pprint(url,res.status_code,sep='--')