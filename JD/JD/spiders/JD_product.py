import scrapy

class JD_productSpider(scrapy.Spider):
    name='Jd_product'
    allowed_domains=['search.jd.com']
    start_urls=['https://search.jd.com/Search?keyword=%E6%95%B0%E7%A0%81&enc=utf-8&wq=%E6%95%B0%E7%A0%81&pvid=34b0fcf7ed434840a74c057bc97be346']

    def parse(self,response):
        pass
