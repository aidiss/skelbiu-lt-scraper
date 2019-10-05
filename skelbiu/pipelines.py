# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy


class SkelbiuPipeline(object):
    def process_item(self, i, spider):
        """Extract pipeline"""

        class Listing(scrapy.Item):
            name = scrapy.Field()
            price = scrapy.Field()
            description = scrapy.Field()
            phone = scrapy.Field()
            url = scrapy.Field()
            timestamp = scrapy.Field()
            redirect_urls = scrapy.Field()
            referer_url = scrapy.Field()

        listing = Listing()
        listing["name"] = i["left-content"].css("h1::text").extract_first().strip()
        try:
            listing["price"] = (
                i["left-content"].css(".price::text").extract_first().strip()
            )
        except:
            pass
        # if item['price']:
        #     item['price'] = item['price'][:-1].split(':')[-1].replace(' ', '').strip()
        # item['description'] = '\n'.join([x for x in item['description'] if x.strip()])

        listing["description"] = (
            i["left-content"].css(".item-description").extract_first().strip()
        )

        listing["phone"] = (
            i["right-content"]
            .css(".phone-button>.primary::text")
            .extract_first()
            .strip()
        )
        listing["timestamp"] = str(i["timestamp"])
        listing["url"] = i["url"]
        listing["redirect_urls"] = i["redirect_urls"]
        listing["referer_url"] = i["referer_url"].decode()
        del i["left-content"]
        del i["right-content"]

        # i = [{k: v.strip()} for k, v in i.items()]
        return listing
