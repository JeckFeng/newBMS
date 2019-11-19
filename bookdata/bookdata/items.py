# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class BookdataItem(scrapy.Item):
    # 书名
    BookName = Field()
    # 作者
    Author = Field()
    # ISBN
    ISBN = Field()
    # 出版社
    Publisher = Field()
    # 出版日期
    Date = Field()
    # 评分
    Score = Field()
    # 图片
    src = Field()
    # 图片标题
    title = Field()



