# import requests
# import base64
# from pprint import pprint
# username='mannan'
# password='admin'
# credential=f'{username}:{password}'
# token=base64.b64encode(credential.encode())
# headers={'Authorization':f'Basic '{token.decode("utf-8")}}
# def wp_pragrphs(text):
#     code=f'<!--wp:paragraph--><p>{text}</p><!--/wp:paragraph-->'
#     return code
# title='What is Lorem Ipsum?'
# prapgraph='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
# Rubel={
#     'title':title,
#     'content':wp_pragrphs(prapgraph),
#     'categories':'102',
# }
# api_endpoint='http://localhost/wp/wp-json/wp/v2/posts'
# r=requests.post(api_endpoint,data=rubel,headers=headers,verify=False)
# import requests
# import base64
# from pprint import pprint
# user='kamal'
# password='admin'
# credential=f'{user}:{password}'
# token=base64.b64decode(credential.encode())
# headers={'Authorization':f'Basic {token.decode("utf-8")}'}
# def wp_pragrphs(text):
#     code=f'<!--wp:paragraph--><p>{text}</p><!--/wp:paragraph-->'
#     return code
# title='What is Lorem Ipsum?'
# paragraph='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
# hasmir={
#     'title':title,
#     'content':wp_pragrphs(paragraph),
#     'categories':'102',

# }
# api_endpoint='http://localhost/wp/wp-json/wp/v2/posts'
# res=requests.post(api_endpoint,data=hasmir,headers=headers, verify=false)
# print(res.status_code)
import requests
import base64
from pprint import pprint
user='Nayem'
password='123456'
credential=f'{user}:{password}'
token=base64.b64decode(credential.encode())
headers={'Authorization':f'Basic {token.decode("utf-8")}'}
def wp_pragrphs(text):
    code=f'<!--wp:paragraph--><p>{text}</p><!--/wp:paragraph-->'
    return code
title='What is loren Ipsum?'
paragrphs='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
api_data={
    'title':title,
    'content':wp_pragrphs(paragrphs),
    'Categories':'102',
}
api_endpoin='http://localhost/wp/wp-json/wp/v2/posts'
res=requests.post(api_endpoin,data=api_data,headers=headers,verify=False)
import requests
import base64
from pprint import pprint
user='noon'
password='123456666'
credential=f'{user}:{password}'
token=base64.b64encode(credential.encode())
headers={'Authorization':f'Basic {token.decode("utf-8")}'}
def wp_pragrphs(text):
    code=f'<!--wp:paragraph--><p>{text}</p><!--/wp:paragraph-->'
    return code
title='What is lorium ipsum?'
paragrphs='This is first paragraphs'
data={
    'title':title,
    'content':wp_pragrphs(paragrphs),
    'categories':'102',
}
api_endspoint='http://localhost/wp/wp-json/wp/v2/posts'
res=requests.post(api_data,data=data,headers=headers,verify=False)
import requests
import base64
from pprint import pprint
user='nama'
password='123456666'
credential=f'{user}:{password}'
token=base64.b64decode(credential.encode())
headers={'Authorization':f'Basice {token.decode("utf-8")}'}
def wp_post(text):
    code=f'<!--wp:paragraph--><p>{text}</p><!--/wp:paragraph-->'
    return code
title='What is epsum'
paragrphs='Ipsum is very important element'
data={
    'title':title,
    'content':wp_post(paragrphs),
    'categories':'102',
}
api_endspoint='http://localhost/wp/wp-json/wp/v2/posts'
res=requests.post(api_endspoint,data=data,headers=headers,verify=False)
import requests
import base64
user='nayem'
password='123456'
credential=f'{user}:{password}'
token=base64.b64decode(credential.encode())
headers={'Authorization':f'Basic {token.decode("utf-8")}'}
def wp_post(text):
    code=f'<!--wp:paragraph--><p>{text}</p><!--/wp:paragraph-->'
    return code
title='What is lorium ipsum'
paragrphs='Lorem Ipsum is simply dummy text of the printing and typesetting industry'
kamal={
    'title':title,
    'content':wp_post(paragrphs),
    'categories':'102'
}
api_data='http://localhost/wp/wp-json/wp/v2/posts'
r=requests.post(api_data,data=kamal,headers=headers,verify=False)