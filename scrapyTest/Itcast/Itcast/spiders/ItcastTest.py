# -*- coding: utf-8 -*-
import scrapy
from Itcast.items import ItcastItem



class ItcasttestSpider(scrapy.Spider):
    name = 'ItcastTest'
    # allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aandroid']

    def parse(self, response):
        # print(response.body)    # 显示网页内容
        item = ItcastItem()       # items.py中定义的数据模板
        node_list = response.xpath("//div[@class='li_txt']")

        for node in node_list:
            name = node.xpath('./h3/text()').extract()
            title = node.xpath('./h4/text()').extract()
            info = node.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # print(name)
            # print(title)
            # print(info)
            # 生成器，逐一返回给引擎，然后引擎返回给pipelines.py分析存储
            yield item
        # pass
