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
DOWNLOAD_DELAY = 5
FEED_EXPORT_ENCODING = "utf-8"
ITEM_PIPELINES = {"skelbiu.pipelines.SkelbiuPipeline": 300}
NEWSPIDER_MODULE = "skelbiu.spiders"
ROBOTSTXT_OBEY = False
SPIDER_MODULES = ["skelbiu.spiders"]
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
LOG_ENABLED = True
LOG_LEVEL = "DEBUG"

DOWNLOADER_MIDDLEWARES = {
    # 'skelbiu.middlewares.CustomProxyMiddleware': 350,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}
ROTATING_PROXY_LIST = [
    '95.28.155.120:8080'
    '200.89.178.40',
    '202.143.121.245:8080',
    '45.234.144.106:8080',
    '78.57.227.227:53281',
    '185.34.52.31:80',
    '62.33.207.202:3128',
]