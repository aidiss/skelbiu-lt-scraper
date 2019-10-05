# -*- coding: utf-8 -*-

# Scrapy settings for skelbiu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

AUTOTHROTTLE_ENABLED = True
BOT_NAME = "skelbiu"
DOWNLOAD_DELAY = 1.2
FEED_EXPORT_ENCODING = "utf-8"
ITEM_PIPELINES = {"skelbiu.pipelines.SkelbiuPipeline": 300}
NEWSPIDER_MODULE = "skelbiu.spiders"
ROBOTSTXT_OBEY = True
SPIDER_MODULES = ["skelbiu.spiders"]
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
