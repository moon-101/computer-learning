# scrapy

## scrapy是什么？
Scrapy 是一个快速的高级**网络爬虫和网络抓取框架**，用于爬取网站并从其页面中提取结构化数据。它可用于广泛的用途，从数据挖掘到监控和自动化测试。
我自己的理解：提取网站信息的应用框架
##  scrapy安装
我个人使用直接用pip Install 安装即可
官方推荐安装方式：如果您使用的是 Anaconda 或 Miniconda，则可以从 conda-forge 频道安装软件包，该频道具有适用于 Linux、Windows 和 macOS 的最新软件包。
### 使用虚拟环境（推荐）
### window系统
### 在ubuntu系统中
总结
scrapy 安装还挺复杂的，不是按操作系统讲解的，而是主要按不同的编辑器按陈述。注：我的安装可能有问题了，只用pip安装，不做前面步骤铺垫，不过影响不大，专业的人也这么安装。



## scrapy的使用
* 1、创建项目
scrapy startproject 项目名称
scrapy结构

    tutorial/
        scrapy.cfg            # deploy configuration file

        tutorial/             # project's Python module, you'll import your code from here
            __init__.py

            items.py          # project items definition file

            middlewares.py    # project middlewares file

            pipelines.py      # project pipelines file

            settings.py       # project settings file

            spiders/          # a directory where you'll later put your spiders
                __init__.py

2、创立文件
在spiders下创建文件

    from pathlib import Path

    import scrapy#导入第三方库


    class QuotesSpider(scrapy.Spider):#爬虫名称
        name = "quotes"#name

        async def start(self):#异步函数
            urls = [
                "https://quotes.toscrape.com/page/1/",
                "https://quotes.toscrape.com/page/2/",
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)#生成器

        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = f"quotes-{page}.html"
            Path(filename).write_bytes(response.body)
            self.log(f"Saved file {filename}")

主要分为两部分“前言”和“parse”


3、运行
scrapy crawl name#或者项目名称


## 提取数据
* 使用Scrapy shell
scrapy shell 'https://quotes.toscrape.com/page/1/'
在windows中 scrapy shell "https://quotes.toscrape.com/page/1/"

对于提取response数据，一共有三种方法，css选择器、re表达式、xpath表达式
这一步是重难点。

css选择器格式写法
    对于class： css(标签.class)
    对于id：css（标签#id）
    对于属性：css(a attr::href)

    response.css(div#id.class.class1 a attr::href)
    
re表达式

xpath表达式



## 存储数据

scrapy crawl name -O name.json
scrapy crawl name -o name.jsonl


## 递推
