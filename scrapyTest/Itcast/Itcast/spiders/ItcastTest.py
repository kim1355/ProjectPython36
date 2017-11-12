# -*- coding: utf-8 -*-
import scrapy


class ItcasttestSpider(scrapy.Spider):
    name = 'ItcastTest'
    # allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aandroid']

    def parse(self, response):
        # print(response.body)    # 显示网页内容

        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            name = node.xpath('./h3/text()').extract()
            title = node.xpath('./h4/text()').extract()
            info = node.xpath('./p/text()').extract()

            print(name)
            print(title)
            print(info)
        # pass
