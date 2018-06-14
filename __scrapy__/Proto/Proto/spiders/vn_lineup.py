# -*- coding: utf-8 -*-
import scrapy
import re
import os
import datetime
from Proto.items import ProtoItem

class ProtoLineupSpider(scrapy.Spider):
    name = 'proto_lineup_id'
    allowed_domains = ['liga-indonesia.id"', ]
    start_urls = [
        "https://www.liga-indonesia.id/",
    ]
    sub_urls = []
    compare_urls = []
    check_match = []
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], self.parse)

    def parse(self, response):
        f = open('for_id_url.txt', 'r')
        for line in f.read().split('\n'):
            self.sub_urls.append(line)
        for line in response.xpath('//div[@class="match-info-extra"]/a[1]'):
            self.compare_urls.append(line.xpath('@href').extract()[0])
        self.sub_urls.pop()

        compare = set(self.compare_urls)
        _return = [x for x in self.sub_urls if x in compare]

        print _return
