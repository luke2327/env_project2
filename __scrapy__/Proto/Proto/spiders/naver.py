# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from Proto.items import ProtoItem

class ProtoSpider(scrapy.Spider):
    name = 'proto_naver'
    allowed_domains = ['sports.naver.com', ]
    start_urls = [
        "http://m.sports.naver.com/kbaseball/news/index.nhn?type=league&league=kbo&isPhoto=N",
    ]

    yesterday_urls = []
    def start_requests(self):
        current_time = datetime.datetime.now()
        if current_time.time().hour >= 15 and current_time.time().hour <= 19:
            for url in self.start_urls:
                self.yesterday_urls.append(url
                 + current_time.strftime("&date=%Y%m%d") + '&page=1')
        for url in self.start_urls + self.yesterday_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoing': 'render.html',
                    'args': {'wait': 1.5}
                }
            })

    def parse(self, response):
        for href in response.xpath('//ul[@class="article_lst"]/li'):
            try:
                item = ProtoItem()
                item['link'] = response.urljoin(href.xpath('a/@href').extract()[0])
                print item['link']
                print '\n\n'
                
            except Exception as e:
                print e
                print '\n\n'
