# scrapy
## 学习心得
* 基础不牢，地动山摇。至今，我有好多概念不懂，模模糊糊，没有个印子。因此不能很好的使用
* 先搭起结构，再不断修饰。我们知道scrapy是一个爬取网站信息的
* 面对一个用scrapy爬取数据的问题时，我们的思考流程是怎么样？
    * 清楚爬取目标信息：到目标网站上，打开网页管理工具f12，分析它处于html文件结构中什么位置，以及需要采取什么方法爬取下来
    * 创建scrapy项目，编写spider项目，items文件、piplines文件
    * 

## scrapy是什么？
Scrapy 是一个快速的高级**网络爬虫和网络抓取框架**，用于爬取网站并从其页面中提取结构化数据。它可用于广泛的用途，从数据挖掘到监控和自动化测试。
我自己的理解：提取网站数据的应用框架
##  scrapy安装
我个人使用直接用pip Install 安装即可，我看过几个软件都推荐Anaconda支持下进行安装，但我嫌麻烦，直接pip安装了，现在也没出过问题。
官方推荐安装方式：如果您使用的是 Anaconda 或 Miniconda，则可以从 conda-forge 频道安装软件包，该频道具有适用于 Linux、Windows 和 macOS 的最新软件包。
### 使用虚拟环境（推荐）
### window系统
### 在ubuntu系统中
总结
scrapy 安装还挺复杂的，不是按操作系统讲解的，而是主要按不同的编辑器按陈述。注：我的安装可能有问题了，只用pip安装，不做前面步骤铺垫，不过影响不大，专业的人也这么安装。

## scrapy的原理
![scrapy架构图](https://www.runoob.com/wp-content/uploads/2018/10/8c591d54457bb033812a2b0364011e9c_articlex.png)"

* Scrapy Engine(引擎): 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。

* Scheduler(调度器): 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。

* Downloader（下载器）：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理，

* Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器).

* Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方。

* Downloader Middlewares（下载中间件）：你可以当作是一个可以自定义扩展下载功能的组件。

* Spider Middlewares（Spider中间件）：你可以理解为是一个可以自定扩展和操作引擎和Spider中间通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）

## scrapy的使用
1. 创建项目
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


2. 创立文件
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

对于提取response数据，其实是两种方法，css选择器、xpath表达式
**这一步是重难点**。

css选择器格式写法
    对于class： css(标签.class)
    对于id：css（标签#id）
    对于属性：css(a attr::href)
示例：
    response.css(div#id.class.class1 a attr::href)

用get(),getall()函数，此外还有re()方法
    
re表达式

xpath表达式



## 存储数据

scrapy crawl name -O name.json
scrapy crawl name -o name.jsonl


## 递推


## scrapy爬取数据的思路