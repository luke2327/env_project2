import scrapy
import re
from Proto.items import ProtoItem

class ProtoSpider(scrapy.Spider):
    name = 'proto_hearth'
    allowed_domains = ['hearthstudy.com', ]
    start_urls = [
        'https://www.hearthstudy.com/',
    ]

    def parse(self, response):
        # url = response.url.split('.')[-2]
        # with open(url, 'wb') as f:
        #     f.write(response.body)

        item = ProtoItem()

        for sel in response.xpath('//div[contains(@class, "bs-callout")]'):
            try:
                item['rank'] = sel.xpath('div/h3/text()').extract()[0].strip()
                if re.search('\d\S+', item['rank']):
                    pass
                else:
                    item = None

                for inner_sel in sel.xpath('div/div[@class="text-left rankdiv"]'):
                    item['link'] = inner_sel.xpath('a/@href').extract()[0].strip()
                    item['title'] =\
                    inner_sel.xpath('a/div[@class="ellipsis-left"]/span/text()')\
                    .extract()[0].strip()

                print item

            except Exception as e:
                pass
