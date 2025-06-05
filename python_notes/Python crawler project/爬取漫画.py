#引入第三方库
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

#爬取网站地址
target_url ="https://www.idmzj.com/view/yaoshenji/41917.html"
chapter_url = "https://www.idmzj.com/info/yaoshenji.html"

#用Selenium获取完整渲染的页面

# 配置浏览器选项
edge_options= Options()
edge_options.add_argument("--ignore-certificate-errors")  # 忽略证书错误
edge_options.add_argument("--disable-gpu")  
edge_options.add_argument("--window-size=1920,1080")
edge_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
service = Service(r'D:\games\edgedriver_win64\msedgedriver.exe') 

#添加浏览器头

driver = webdriver.Edge(service=service,options=edge_options)
try:
    driver.get(chapter_url)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all('span', class_='list_con_zj')
    chapter_list=[]
    for elem  in elements:
        chapter_list.append(elem.text.strip())
    print(chapter_list)

except Exception as e:
    print("失败，",e)

finally:
    driver.quit()








