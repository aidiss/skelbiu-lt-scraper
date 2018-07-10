# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['skelbiu.lt']
    start_urls = ['https://www.skelbiu.lt/skelbimai/kompiuterija/kompiuteriai/1']

    rules = (
        Rule(LinkExtractor(allow=r'lt/skelbimai/kompiuterija/kompiuteriai/[0-9].*'), follow=True),
        Rule(LinkExtractor(restrict_css='li.simpleAds'), callback='parse_item'),
    )

    def parse_item(self, r):
        i = {}
        i['add_id'] = r.css('#adID::text').extract_first()
        i['title'] = r.css('#adTitle > h1::text').extract_first()
        i['description'] = r.css('#adDescription::text').extract()
        i['price'] = r.css('div.announcementPrice h2::text').extract_first()
        i['photo'] = r.css('#photo-place::attr(src)').extract_first()
        i['image_list'] = r.css('#imagesList > div > a::attr(href)').extract()
        yield i
