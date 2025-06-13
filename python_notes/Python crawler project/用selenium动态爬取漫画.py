#爬取漫画
"""因为这是动态内容，不适合request库爬取、因此我们采用selenum动态爬取"""
#引入第三方库
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service as edge_service #驱动路径
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os
import logging

logging.basicConfig(level=logging.INFO)
#创建漫画目录
base_directory = r'D:\games\computer-learning\爬取的漫画'
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

#目标目录
target_directory=os.path.join(base_directory,'暴走邻家')
if not os.path.exists(target_directory):
    os.makedirs(target_directory)
    print(f"{target_directory}已创建")
else:
    print("已存在")

# 配置 Edge 选项
options = webdriver.EdgeOptions()
options.add_argument('--ignore-certificate-errors')
service = edge_service(executable_path=r"D:\games\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=options)

#确认爬取网站
targer_url ='https://www.manhuazhan.com/chapter/495475-154500.html'


#打开一个网站
driver.get(targer_url)

#隐形等待10秒
driver.implicitly_wait(10)

#解决掉反爬虫机制
# 逐步滚动页面（每次滚动一屏高度）
scroll_height = driver.execute_script("return document.body.scrollHeight")
for i in range(0, scroll_height, 800):
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(0.5)  # 滚动间隔防封IP

try:
    img_elements = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,'lazy')))
    if img_elements:
        for i ,img in enumerate(img_elements):
            img_url = img.get_attribute('src')

            # 下载图片
            img_ = requests.get(img_url)
            filename = os.path.join(target_directory, f"{i}.jpg")
            with open(filename, 'wb') as f:
                f.write(img_.content)
    else:
        print("未找到图片元素")
finally:
    driver.quit()