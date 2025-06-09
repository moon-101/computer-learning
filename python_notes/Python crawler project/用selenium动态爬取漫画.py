#爬取漫画
"""因为这是动态内容，不适合request库爬取、因此我们采用selenum动态爬取"""
#引入第三方库
from selenium import webdriver
from selenium.webdriver.edge.service import service as edge_service #驱动路径
from bs4 import BeautifulSoup
import time

service= edge_service()
options=webdriver.EdgeOptions()
driver= webdriver.Edge(service=service,options=options)

#确认爬取网站
targer_url ='https://www.idmzj.com/info/yaoshenji.html'

#打开一个网站
driver.get(targer_url)

# 等待页面加载完成
time.sleep(2)  # 可以根据需要调整等待时间

# 强制停止页面加载
driver.execute_script("window.stop();")
# 获取页面标题
print(driver.title)


#解析网站内容
bs = BeautifulSoup(r.text,'lxml')
print(bs)
list_con_li = bs.find('ul',class_='list_con_li')
#处理清洗数据

#存储数据



