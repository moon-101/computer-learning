import requests
from bs4 import BeautifulSoup
import lxml
import chardet
import time
import random
import os
import json
from fake_useragent import UserAgent
from tqdm import tqdm
import string
url="https://www.22biqu.com/biqu13446/12278419.html"
response=requests.get(url)

response.raise_for_status()

#自动检察编码
det= chardet.detect(response.content)
actual_encoding=det['encoding']
print(f"编码：{actual_encoding}")

#使用正确编码解码
response.encoding = actual_encoding
html_content = response.text

#解析内容
soup=BeautifulSoup(html_content,'lxml')
title= soup.find("h1",class_='title')
#test

print(title)