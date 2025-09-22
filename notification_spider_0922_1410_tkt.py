# 代码生成时间: 2025-09-22 14:10:31
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider
from scrapy.utils.log import configure_logging

# 设置日志配置
configure_logging(install_root_handler=False)

class NotificationSpider(scrapy.Spider):
    name = "notification_spider"
    allowed_domains = ["example.com"]  # 假设消息来源网站
    start_urls = [
        "http://example.com/notification"  # 假设的消息通知页面URL
    ]

    def parse(self, response):
        # 解析响应并提取消息
        try:
            notifications = response.css("div.notification::text").getall()
            for notification in notifications:
                yield {
                    "message": notification.strip()
                }
        except Exception as e:
            # 错误处理
            self.logger.error(f"Error parsing notifications: {e}")
            raise CloseSpider(f"Error parsing notifications: {e}")

    def closed(self, reason):
        # 爬虫关闭时执行的操作，例如发送通知
        self.logger.info(f"Spider closed with reason: {reason}")


# 爬虫运行配置
class NotificationSpiderProcess:
    def __init__(self):
        self.process = CrawlerProcess()

    def add_spider(self, spider):
        self.process.crawl(spider)

    def start(self):
        self.process.start()


if __name__ == "__main__":
    # 创建爬虫运行配置实例
    notification_process = NotificationSpiderProcess()
    # 添加爬虫
    notification_process.add_spider(NotificationSpider)
    # 启动爬虫
    notification_process.start()