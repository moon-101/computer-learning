from pathlib import Path
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,  # 忽略 robots.txt 文件
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)  # 修正拼写错误
        self.log(f"Saved file {filename}")
