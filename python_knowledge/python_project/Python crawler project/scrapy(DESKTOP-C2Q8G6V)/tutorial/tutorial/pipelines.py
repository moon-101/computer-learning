# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

class SaveToFilePipeline:
    def process_item(self, item, spider):
        # 确保 'downloads' 目录存在
        os.makedirs('downloads', exist_ok=True)
        filename = item['filename']
        with open(os.path.join('downloads', filename), 'w', encoding='utf-8') as f:
            f.write(item['content'])
        return item
