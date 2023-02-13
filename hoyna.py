import requests
from pprint import pprint
from pprint import pprint
base_url='https://blogdelacalidad.com/wp-json/wp/v2'
page_api=f'{base_url}/pages'
# post_api=f'{base_url}/posts'
res=requests.get(page_api)
pprint(res.json())