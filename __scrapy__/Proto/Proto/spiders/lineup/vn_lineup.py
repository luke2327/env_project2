# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from Proto.items import ProtoItem

class ProtoLineupSpider(scrapy.Spider):
    name = 'proto_lineup_vn'
    allowed_domains = ['goal.com', ]
    start_urls = [
        "http://www.goal.com/vn/vleague-1/lichthidau-ketqua/tuan-10/aho73e5udydy96iun3tkzdzsi",
    ]

    yesterday_urls = []
    def start_requests(self):
        yield scrapy.Request(url, self.parse, meta ='')

    def parse(self, response):
        try:
            for match in response.xpath('//div[@class="match-status"]/time'):
                print match.xpath('text()').extract()[0]
        except Exception:
            pass
