#爬取漫画
"""因为这是动态内容，不适合request库爬取、因此我们采用selenum动态爬取"""
#引入第三方库
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service as edge_service #驱动路径
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

service= edge_service(executable_path=r"D:\games\edgedriver_win64\msedgedriver.exe")
options=webdriver.EdgeOptions()
driver= webdriver.Edge(service=service,options=options)

#确认爬取网站
targer_url ='https://www.idmzj.com/view/yaoshenji/41917.html'

#隐形等待10秒
driver.implicitly_wait(10)

#解决掉反爬虫机制
# 逐步滚动页面（每次滚动一屏高度）
scroll_height = driver.execute_script("return document.body.scrollHeight")
for i in range(0, scroll_height, 800):
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(0.5)  # 滚动间隔防封IP

#打开一个网站
driver.get(targer_url)

#定位元素
img = driver.find_element(By.CLASS_NAME,'scrollbar-demo-item')

#元素操作
img_url = img.get_attribute('src')

#下载图片
img_=requests.get(img_url)
with open("manhua.jpg",'wb') as f:
    f.write(img_.content)


driver.quit()

#解析网站内容

#处理清洗数据

#存储数据
# 获取页面标题




