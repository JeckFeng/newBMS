# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request
from bookdata.items import BookdataItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/小说?start=0&type=T']

    def parse(self, response):
        # 获取下一页的数据
        tag = ['小说']
        for j in tag:
            for i in range(1):
                next_url = 'https://book.douban.com' + '/tag/'+j+'?start=' + str(20 * i) + '&type=T'
                yield Request(next_url, callback=self.parse_2)

    def parse_2(self, response):
        # 获取每个Item的详细信息网页链接
        item_url = response.xpath('//*[@class="nbg"]/@href').extract()
        for url in item_url:
            yield Request(url, callback=self.getdata)

    def getdata(self, response):
        item = BookdataItem()

        info = response.css('div#info').xpath('string(.)').extract_first()
        keys = [s.strip().replace(':', '')
                for s in response.css('div#info span.pl::text').extract()]
        values = [re.sub(r'\s+', '', s.strip())
                  for s in re.split(r'\s*(?:%s):\s*' % '|'.join(keys), info)][1:]

        information = dict(zip(keys, values))
        # 书名
        item['BookName'] = response.xpath(
            '//*[@id="wrapper"]/h1/span/text()').extract_first()
        # 作者
        item['Author'] = information['作者']

        # ISBN
        item['ISBN'] = information['ISBN']
        # 出版社
        item['Publisher'] = information['出版社']
        # 出版日期
        item['Date'] = information['出版年']
        # 评分
        item['Score'] = response.xpath(
            '//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
        
        

        title = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
        src = response.xpath('//*[@id="mainpic"]/a/img/@src').extract_first()

        item['title'] = title
        item['src'] = src
        
        yield item
