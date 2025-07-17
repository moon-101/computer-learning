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
