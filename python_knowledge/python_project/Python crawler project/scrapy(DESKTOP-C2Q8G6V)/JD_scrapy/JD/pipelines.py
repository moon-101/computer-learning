# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from SmartCraneHub.items import SmartcranehubItem
import logging

class SmartcranehubPipeline(object):
    def open_spider(self,spider):
        self.client=pymongo.MongoClient("mongoab://localhost/",27017)
        #s
        self.db=self.client['SmartSpiderHubTest']
        self.collection=self.db['Lingshi']
    
    def close_spider(self,spider):
        self.client.close()
    
    def process_item(self,item,spider):

        if isinstance(item,SmartcranehubItem):
            try:
                collection_name=self.getCollection(item['goods_brand'])
                old_item=self.db[collection_name].find_one({goods_id})
                if old_item is None:
                    logging.info('items'+item['goods_id']+'insert in'+collection_name+'db.')
                    self.db[collection_name].insert(dict(item))
                elif self.needToUpdate(old_item,item):
                    self.db[collection_name].remove({'goods_id':item['goods_id']})
                    self.db[collection_name].insert(dict(item))
                    logging.info("items:"+item['goods_id']+"has UPDATED in"+collection_name+'db.')
                else:
                    logging.info('items:'+item['goods_id']+'has in'+collection_name+'db.')
            
            except Exception as e:
                logging.error("PIPELINE EXCEPTION:"+str(e))
        return item
    
    def getCollection(self,brand):
        if brand=='乐事':
            return 'leshi'
        elif brand=='汪汪':
            return 'wangwang'
        elif brand=='三只松鼠':
            return 'Sanzhisongshu'
        elif brand=='卫龙':
            return 'weilong'
        elif brand=='口水娃':
            return 'koisjiowa'
        elif brand=='奥利奥':
            return 'Aoliao'
        elif brand=='良品铺子':
            return 'Liangpinpuzi'
        else:
            return 'Lingshi'
            

    
    def needToUpdate(self,old_item,new_item):
        if old_item['goods_price']!=new_item['goods_price']:
            old_time=old_item['goods_time']
            old_price=float(old_item['goods_price'])
            new_price=float(new_item['goods_price'])

            minus_price=round((new_price-old_price),2)
            logging.info('Need To Update')

            if minus_price>=0:
                new_item['goods_describe']='比' +old_time+'涨了'+str(minus_price)+'元。'
            else:
                new_item['goods_describe']='比'+old_time+'降了'+str(minus_price)+'元。'
            return True
        return False
