# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BookdataItem
import re


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='https://book.douban.com'+'//*[contains(@class,"next")]')),
	    Rule(LinkExtractor(restrict_xpaths='//*[@class="nbg"]'),callback = 'parse_item')
    )

    def parse_item(self, response):
        item = BookdataItem()

        info = response.css('div#info').xpath('string(.)').extract_first()
        keys = [s.strip().replace(':', '') for s in response.css('div#info span.pl::text').extract()]
        values = [re.sub('\s+', '', s.strip()) for s in re.split('\s*(?:%s):\s*' % '|'.join(keys), info)][1:]

        information = dict(zip(keys,values))
        # 书名
        item['BookName'] = response.xpath(
            '//*[@id="wrapper"]/h1/span/text()').extract()
        # 作者
        item['Author'] = information['作者']

        # ISBN
        item['ISBN'] = information['ISBN']
        # 出版社
        item[' Publisher'] =  information['出版社']
        # 出版日期
        item['Data'] = information['出版年']
        # 评分
        item['Score'] =  response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()

        yield item
