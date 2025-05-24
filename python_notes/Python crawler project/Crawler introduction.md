# 网络爬虫的介绍
## 一、什么是网络爬虫？
爬虫：一段自动抓取互联网信息的程序，从互联网上抓取对于我们有价值的信息。  
#按照我的自己私人理解，其实就是收集各个网站信息的程序之名。
## 二、网络爬虫的原理
* 发送http请求：爬虫通过http请求从目标网站获取html页面，常用的库有requests
* 解析内容：获取html页面后，爬虫需要解析内容并提取数据，常用的库有Beautifulsoup、lxml、Scrapy等。
* 提取数据：通过定位html元素（如标签、属性、类名等）来提取所需的数据。
* 存储数据：将提取的数据存储到数据库、CSV文件、JSON文件等格式中、以便后续使用或分析。
## 三、爬虫的工具
*工欲善其事，必先利其器*
1、request + beautifulsoup4  

    request库 负责请求
    beautifulsoup4 负责解析
### 3.1beautifulsoup4
1、安装bs4  
方法：pip安装
pip install beautifulsoup4
pip install lxml#推荐使用lxml作为解析器（速度更快）
2、基本用法
BeautifulSoup 用于解析 HTML 或 XML 数据，并提供了一些方法来导航、搜索和修改解析树。
BeautifulSoup 常见的操作包括查找标签、获取标签属性、提取文本等。
要使用 BeautifulSoup，需要先导入 BeautifulSoup，并将 HTML 页面加载到 BeautifulSoup 对象中。
通常，你会先用爬虫库（如 requests）获取网页内容:
    
     ```python
      #确认需要爬取的网站网址
      url=""

     #发送网站请求，（已下载）
     response = requests.get(url)

     #确认编码格式
     response.encoding="utf-8"

     #解析内容
     soup=Beautitulsoup(response.text,"lxml")

     #提取内容
     neirong= soup.find('',id='')

     #存储内容
     with open('file name','moshi') as f:
        f.write(soup,w),encoding=''utf-8'）
     ```
大体结构如上
#由于各种原因会不断细化这四个环节。比如代码重构，模块化处理，模拟网络请求头，反爬虫机制、测试重写等等。但是，主体结构就是这四个。

*遭遇到403情况，模拟网络请求头
*乱码问题




