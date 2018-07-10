# -*- coding: utf-8 -*-

# Scrapy settings for skelbiu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'skelbiu'
DOWNLOAD_DELAY = 1
SPIDER_MODULES = ['skelbiu.spiders']
NEWSPIDER_MODULE = 'skelbiu.spiders'
USER_AGENT = ''
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {'skelbiu.pipelines.SkelbiuPipeline': 300}
AUTOTHROTTLE_ENABLED = True
