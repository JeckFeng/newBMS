# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImagesPipeline(ImagesPipeline):
    
    # 发生图片下载请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['src'], meta={'item': item})
    
    def file_path(self, request, response=None, info=None):
        # 接收上面meta传递过来的图片名称
        item = request.meta['item']
        # 提取url前面名称作为图片名
        image_name = item['src'].split('/')[-1]
        
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        path = item['title'] + image_name
        
        return path


class SQLitePipeline(object):
    def open_spider(self, spider):
        self.db = sqlite3.connect('F:/pycharm项目/图书管理系统NEW/AllDataBase/book.db')
        self.db_cur = self.db.cursor()

        sql1 = '''CREATE TABLE IF NOT EXISTS [BookData](
                                        [ISBN] INT(15) PRIMARY KEY NOT NULL,
                                        [BookName] CHAR(12) NOT NULL,
                                        [Author] CHAR(12) NOT NULL,
                                        [Publisher] CHAR(20),
                                        [Date] DATE,
                                        [Score] FLOAT(4));
                                        

                            '''
        self.db_cur.execute(sql1)

        
    def close_spider(self):
        
        self.db.close()
        
        
    def process_item(self,item,spider):
        self.insert_db(item)
        
        return item
    
    def insert_db(self,item):
        values = (
            item['ISBN'],
            item['BookName'],
            item['Author'],
            item['Publisher'],
            item['Date'],
            item['Score'],
            
        )

        sql = 'INSERT OR IGNORE into BookData(ISBN,BookName,Author,Publisher,Date,Score) values("%s","%s","%s","%s","%s","%s")' % (
            values[0],values[1],values[2],values[3],values[4],values[5])


        self.db_cur.execute(sql)
        print('提示：'+'\n')
        print('**'+'\n',
              '*-----------------------------------------插入成功--------------------------------------------*'+'\n','**')
            
        self.db.commit()


