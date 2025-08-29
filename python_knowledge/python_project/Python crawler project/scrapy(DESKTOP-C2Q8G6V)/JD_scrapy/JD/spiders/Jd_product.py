import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
import re
from ..items import SmartcranehubItem
import datetime
import lxml

class JD_productSpider(scrapy.Spider):
    name='Jd_product'
    allowed_domains=['search.jd.com']
    max_page=100
    start_urls=['https://search.jd.com/Search?keyword=%E9%9B%B6%E9%A3%9F&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=lingshi&stock=1&click=0&page=1']

    def parse(self,response):
        content =response.body
        soup =BeautifulSoup(content,'lxml')
        brand_temp_list =soup.find_all('li',attrs={'id':re.compile(r'brand-(\w+)')})
        brand_list=list()
        if 'risk_handler' in response.url:
            self.logger.warning("触发京东反爬机制！请检查爬虫配置")
        return  # 放弃当前请求
        for item in brand_temp_list:
            brand_title= item.find('a')["title"]
            brand_list.append(re.sub(r"[A-za-z0-9\!\%\[\]\,\.\(\)\(\)\"\.\'\]","",brand_title))
            # brand_list= li
            goods_temp_list=soup.find_all('li',attrs={'class':'gl-item'})
            for item in goods_temp_list:
                goods=SmartcranehubItem()
                #零食 id
                goods_id=item['data-pid']
                #零食 prcie
                goods_price=item.find_all('div',attrs={'class':'p-price'})


                #零食 tilte
                goods_temp_title=item.find_all('div',attrs={'class':'p-name'})
                goods_title=goods_temp_title[0].find('em').text

                #零食 img
                goods_temp_img=item.find_all('div',class_='p-img')
                goods_img='http:'+goods_temp_img[0].find('img')['source-data-lazy-img']['src']

                #零食 url
                goods_temp_url=item.find('div',class_='p-img').find('a',attrs={'target':'blank'})['href']
                goods_url=goods_temp_url if 'http' in goods_temp_url else 'https:'+goods_temp_url

                #零食 price
                goods_price=item.find_all()

                # 零食 brand
                goods_brand= self.getGoodsBrand(goods_title,brand_list)

                # 零食 time
                cur_time= datetime.datetime.now()
                cur_year=str(cur_time.year)
                cur_month=str(cur_time.month) if len(str(cur_time.month))==2 else '0'+str(cur_time.month)
                goods_time=cur_year +'-'+cur_month+'-'+cur_day

                # 零食 描述
                goods['goods_id']=goods_id
                goods['goods_title']=goods_title
                goods['goods_url']=goods_url
                goods['goods_img']=goods_img
                goods['goods_price']=goods_price
                goods['goods_shop']=goods_shop
                goods['goods_time']=goods_time
                goods['goods_brand']=goods_brand
                goods['goods_describe']=goods_describe
                yield goods

        cur_page_num=int(response.url.split('&page=')[1])
        next_page_num=cur_page_num+1
        if cur_page_num<self.max_page:
            next_url=response.url[:-len(str(cur_page_num))]+str(next_page_num)
            yield Request(url=next_url,callback=self.parse,dont_filter=True)


            
        def getGoodBrand(self,goods_title,brand_list):
            for brand in brand_list:
                if brand in goods_title:
                    return brand
            return 'No-brand'



