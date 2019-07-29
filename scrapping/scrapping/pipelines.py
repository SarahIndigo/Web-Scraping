# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# scraped data -> item containers -> file csv/xml/json
# scraped data -> item containers -> Pipeline -> SQL/Mongo database

import pymongo

class QuotetutorialPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost',27017)
        db = self.conn['database_name']
        self.collection = db['collection_name']

    def process_item(self, item, spider):
        #print("pipeline :" + item['title'][0])
        self.collection.insert(dict(item))
        return item
