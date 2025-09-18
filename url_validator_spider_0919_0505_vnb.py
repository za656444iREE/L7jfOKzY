# 代码生成时间: 2025-09-19 05:05:31
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy import signals
from w3lib.url import is_valid_url
import logging


# 设置日志
logger = logging.getLogger(__name__)


class URLValidatorSpider(Spider):
    name = 'url_validator'
    allowed_domains = []  # 允许抓取的域名列表
    start_urls = []  # 需要验证的URL列表

    def __init__(self, url_list=None, *args, **kwargs):
        # 确保提供了URL列表
        if not isinstance(url_list, list):
            logger.error('URL list must be provided.')
            raise NotConfigured('URL list must be provided.')
        self.start_urls = url_list
        super().__init__(*args, **kwargs)

    def parse(self, response):
        # 验证URL是否有效
        if is_valid_url(response.url):
            yield {
                'url': response.url,
                'status': 'valid'
            }
        else:
            yield {
                'url': response.url,
                'status': 'invalid'
            }

    def start_requests(self):
        # 对于每个URL，生成一个Request对象
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

# 定义一个函数来启动爬虫
def start_spider(url_list):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    })
    process.crawl(URLValidatorSpider, url_list=url_list)
    process.start()  # 启动爬虫

# 以下是启动爬虫的示例代码
if __name__ == '__main__':
    # 提供需要验证的URL列表
    url_list = [
        'https://www.example.com',
        'http://invalid-url-without-schema',
        'https://www.google.com'
    ]
    start_spider(url_list)