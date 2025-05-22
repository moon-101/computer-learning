"""
def display_message():
    print("函数的定义，形参和实参")
#8.2
def favorite_book(title):
    print(title)
favorite_book('One of my favorite books is Alice in Wonderland')
"""
"""
#8.3
def make_shirt(chima='smsm',zhi='I Love Python'):
    print(f"{chima},{zhi}")
make_shirt('L')
make_shirt(chima='m')
make_shirt(zhi='ccc',chima='kendingyou')
#8.4
"""
"""
#8.5
def describe_city(city,country='qing'):
    print(f"{city} is in {country}")
describe_city('beijing','china')
describe_city('shanghai')
describe_city('changan','tang danasty')
"""
"""
#8.6
def city_country(city,country):
    print(f"“{city},{country}”")
city_country("luoyang","hang")
city_country("xian",'qing')
city_country("bianliang","song")
"""
"""
#8.7
def make_album(name,value,number=None):
    zhuanji={}
    zhuanji['zhuozhe']=name
    zhuanji['zhuoping']=value
    if number!=None:
        zhuanji['shuliang']=number
    return zhuanji

#8.8
print('qkeyituichuqu')
while True:
    name=input('name')
    if name=='q':
        break
    zhuanji=input('zhuangji')
    if zhuanji=='q':
        break
    print(make_album(name,zhuanji))
"""
"""
#8.9
list_1=['你的好','我好']
def show_messages(messages):
    send_messages=[]
    for i in messages:
        print(i)
        send_messages.append(i)
    return
        
def send_messages(list):
    sent_message=[]
    x=list[:]
    for message in x:
        print (message)
        sent_message.append(message)
    print(x)
    return  print(list)

show_messages(list_1)
send_messages(list_1)
#8.10
#8.11
"""
"""
#8.12
def sandice(*foods):
    print(foods)

sandice('apple')
sandice('banana')
sandice('li')
"""
#8.13
def bulid_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=bulid_profile('albert','sfsdf',
                           location='princeton',
                           field='physics')

my_profile=bulid_profile('li','yanfen',
                         location='china',
                         like='book')
print(my_profile)
#8.14
def cat_imformation(zhizhaoshang,xinhao,**duoyun):
    duoyun['zhi']=zhizhaoshang
    duoyun['book']=xinhao
    return duoyun
my_car=cat_imformation('cc','bbb',
                       color='fsfsf',
                        xinghao='sfsf')
print(my_car)

#8.15
from printing_functions import zzz
#8.15
import zzz
from print import zzz as zz
from zzzxcv import *

