# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SkelbiuPipeline(object):
    def process_item(self, item, spider):
        if item['price']:
            item['price'] = item['price'][:-1].split(':')[-1].replace(' ', '').strip()
        item['description'] = '\n'.join([x for x in item['description'] if x.strip()])
        return item
