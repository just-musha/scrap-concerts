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

            url = one_json["url"]
            print("\n\n ------ ONE:\n", one_json)
            yield scrapy.Request(url, callback=self.get_description, meta={'item': {
                'date': one_json["startDate"],
                'name': one_json["name"]
            }})

    def get_description(self, response):
        item = response.meta['item']
        print('item = ', item)

        desc = response.xpath("/html/body/div['wrapper']/main/div['event-description-holder']/div['container']/div['readable-column']/div['event-description-text']/p/text()").extract()
        item['description'] = desc

        short_url = response.xpath("/html/body/div['wrapper']/main/div['event-main-info-holder']/div['container']/div['event-info-holder-image-big']/img/@src").extract_first()
        url = "https://" + self.allowed_domains[0] + short_url

        item['image_urls'] = [url]
        return item
