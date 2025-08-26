from pathlib import Path
import requests
from bs4 import BeautifulSoup 
import lxml
import scrapy#导入第三方库


url=r"https://newssearch.chinadaily.com.cn/en/search?cond=%7B%22publishedDateFrom%22%3A%222012-02-01%22%2C%22publishedDateTo%22%3A%222012-12-31%22%2C%22sort%22%3A%22dp%22%2C%22duplication%22%3A%22off%22%7D&language=en"

response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
result=soup.find('span',{'class':'insto'}).find_all('a',{'attr':'href'})
url_all=[tag['href'] for tag in result]

class QuotesSpider(scrapy.Spider):#爬虫名称
    name = "china_daily"#name

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
