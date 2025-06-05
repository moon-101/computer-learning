# 网络爬虫的介绍
## 一、什么是网络爬虫？
爬虫：一段自动抓取互联网信息的程序，从互联网上抓取对于我们有价值的信息。  
#按照我的自己私人理解，其实就是收集各个网站信息的程序之名。
***

## 二、网络爬虫的原理
* 发送http请求：爬虫通过http请求从目标网站获取html页面，常用的库有requests
* 解析内容：获取html页面后，爬虫需要解析内容并提取数据，常用的库有Beautifulsoup、lxml、Scrapy等。
* 提取数据：通过定位html元素（如标签、属性、类名等）来提取所需的数据。
* 存储数据：将提取的数据存储到数据库、CSV文件、JSON文件等格式中、以便后续使用或分析。

***
## 三、爬虫的工具以及如何使用爬虫
*工欲善其事，必先利其器*
### 3.1 request + beautifulsoup4  运用

request库 负责请求网站响应
beautifulsoup4 负责解析网站内容

#### 3.1.1 beautifulsoup4
##### 1、bs4的介绍
BeautifulSoup 用于解析 HTML 或 XML 数据，并提供了一些方法来导航、搜索和修改解析树。

##### 2、安装bs4  
方法：pip安装

    pip install beautifulsoup4
    pip install lxml#推荐使用lxml作为解析器（速度更快）

##### 3、基本用法
BeautifulSoup 常见的操作包括查找标签、获取标签属性、提取文本等。
使用 BeautifulSoup，需要先导入 BeautifulSoup，并将 HTML 页面加载到 BeautifulSoup 对象中。
通常，你会先用爬虫库（如 requests）获取网页内容:
    
     import requests
     from BeautifulSoup import bs4
     import lxml

     python
     #模拟随机网络请求头
     *如果不使用模拟随机网络请求头，容易致使ip封禁，网站请求失效*

     #确认需要爬取的网站网址
     url=""

     #发送网站请求
     response = requests.get(url)

     #确认编码格式
     *编码一般是"utf-8",如果乱码，则需要检测一下网站编码格式
     response.encoding="utf-8"


     #解析内容
     soup=Beautitulsoup(response.text,"lxml")

     #提取内容
     content= soup.find('',id='')

     """处理内容
     这个处理十分复杂，我们分类讨论
     对于文本，使用get_text()函数处理

     clean_content=content.get_text()

     #存储内容
     with open('file name','moshi') as f:
        f.write(soup,w),encoding=''utf-8'）

     
大体结构如上
#由于各种原因会不断细化这四个环节。比如代码重构，模块化处理，模拟网络请求头，反爬虫机制、测试重写等等。但是，主体结构就是这四个。
实际上操作会有各种各样的问题如：
* 遭遇到403情况，模拟网络请求头
* 乱码问题，确认编码
* 快速大量请求，被ip屏蔽，随机访问延迟
* 创建目录文件，提取标题和正文，循环递增创建文件
* 等等

 ##### 4、实例分析

下面我们以爬取小说《许仙志》实例具体讲解
存储内容
 
*初级爬虫方法，requests+bs4爬取网站信息*

    #引入第三方库
    import requests
    from bs4 import BeautifulSoup
    import lxml #lxml,便于快速解析
    import chardet #自动检测编码格式
    import time #时间
    import random #随机
    import os #文件创建
    import json 
    from fake_useragent import UserAgent #随机网络请求头
    from tqdm import tqdm  #下载可视化体现
    import string

    #模拟请求头
    headers = {
        'User-Agent': UserAgent().random,  # 每次请求生成随机UA
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.22biqu.com/',
        'DNT': '1'  # 禁止追踪
    }

    #创建基准目录，预设存储文件路径，简化循环递进
    base_directory = r'D:\games\computer-learning\爬取的小说'
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)


    #目标目录，
    target_directory=os.path.join(base_directory,'许仙志')
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        print(f"{target_directory}已创建")
    else:
        print("已存在")
    
    #确定最小、最大时间间隔
    min_interval=1
    max_interval=5

    #tqdm开始计算
    for i in tqdm(range(12278419, 12278429), 
                desc="正在爬取小说", 
                unit="章",
                ncols=100,
                dynamic_ncols=True):

        #测试异常，防止异常后，程序直接卡死
        try:
            url=f"https://www.22biqu.com/biqu13446/{i}.html"
            #由于要爬取的内容，有时部分存在在下一页中
            url2=f"https://www.22biqu.com/biqu13446/{i}_2.html"

            #请求网站，获取原始内容
            response=requests.get(url,headers=headers)
            
            #检查HTTP请求的响应状态码
            response.raise_for_status()
            
            #自动检察编码
            det= chardet.detect(response.content)


            #使用正确编码解码
            response.encoding = det
            html_content = response.text

            #解析内容
            soup=BeautifulSoup(html_content,'lxml')
            
            #添加随机访问时间间隔
            interval= random.uniform(min_interval,max_interval)

            #获取章节标题
            title_tag = soup.find("h1",class_='title')

            #这而用了一大堆简写语法，
            raw_title = title_tag.get_text().strip() 
            if title_tag ：
                print(raw_title)
            else ：
                raw_title=f"第{i-12278418}章"

            cleaned_title =raw_title

            """     clean_filename=raw_title

            # 加强版文件名清理
            def clean_filename(title):
                # 替换常见非法字符
                title = title.replace('\n', '').replace('\r', '').strip()
                # 只保留允许的字符
                valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
                cleaned = ''.join(c for c in title if c in valid_chars)
                # 确保不为空
                return cleaned or f"第{i-12278418}章"
            """

            #是否有下一页
            response_2=requests.get(url2,headers=headers)

            # 确保目录存在
            os.makedirs(target_directory, exist_ok=True)

            #获取正文内容
            content_div=soup.find("div",id='content')
            if content_div:
                #清理文本内容
                text_content = content_div.get_text()

                # 优化后的处理逻辑
                cleaned_content = '\n'.join(
                    ('　　' + line.strip() if i == 0 else line.strip())  # 仅每段段落首行缩进2字符
                    for i, line in enumerate(
                        text_content.replace('\r', '').split('\n\n')  # 按段落分割
                    ) if line.strip()
                )

                #保存为单独文件
                filename = os.path.join(target_directory, f"{cleaned_title}.txt")
                with open(filename,encoding='utf-8',mode='w') as f:
                    f.write(cleaned_content)
                
                if  response_2:
                    soup_2= BeautifulSoup(response_2.text,'lxml')
                    houxu=soup_2.find("div",id='content').get_text()
                    houxu = '\n'.join(
                    ('　　' + line.strip() if i == 0 else line.strip())  # 仅首行缩进
                    for i, line in enumerate(
                        text_content.replace('\r', '').split('\n\n')  # 按段落分割
                    ) if line.strip()
                )


                    with open(filename,encoding='utf-8',mode='a') as f:
                        f.write(houxu)   
                else:         
                    print(f"小说{cleaned_title}保存完成")
            else:
                print("未完成")
            
            #随机时间暂停
            time.sleep(interval)

        except Exception as e:
            tqdm.write((f"处理{url}发生错误：{e}"))
            continue
            、、、
### 3.2 Scapy 运用










