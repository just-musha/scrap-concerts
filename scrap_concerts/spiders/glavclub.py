# -*- coding: utf-8 -*-
import scrapy
import json

from scrap_concerts.items import ScrapConcertsItem

class GlavclubSpider(scrapy.Spider):
    name = 'glavclub'
    allowed_domains = ['glavclub.com']
    start_urls = ['https://glavclub.com/#afisha']

    # Enable Feed Storage
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'file:///tmp/%(time)s.json'
    }

    def parse(self, response):

        for one in response.xpath('//main//script["application/ld+json"]/text()').getall():
            one_json = json.loads(one)

            # scrapy.Request(one_json["url"], callback=self.get_description)
            #
            # sci = ScrapConcertsItem(
            #     date = one_json["startDate"],
            #     name = one_json["name"]
            # )
            # print("SCI = ", sci)
            # yield sci

            url = one_json["url"]
            print("\n\n ------ ONE:\n", one_json)
            yield scrapy.Request(url, callback=get_description, meta={'item': {
                'date': one_json["startDate"],
                'name': one_json["name"]
            }})

def get_description(response):
    item = response.meta['item']
    print('item = ', item)
    #desc = response.xpath("/html/body/div['wrapper']/main//div['readable-column']/div['event-description-text']/p/text()").extract_first()
    desc = response.xpath("/html/body/div['wrapper']/main/div['event-description-holder']/div['container']/div['readable-column']/div['event-description-text']/p/text()").extract()
    item['description'] = desc
    print("\n ------ DESC = ", desc)
    return item
