# 代码生成时间: 2025-09-20 02:14:11
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

# 进程管理器类
class ProcessManager:
    def __init__(self):
        # 配置日志
        configure_logging({'LOG_LEVEL': 'INFO'})
        # 初始化Scrapy进程
        self.process = CrawlerProcess(get_project_settings())
        
    def run_spider(self, spider_cls):
        """运行指定的爬虫"""
        try:
            # 启动爬虫
            self.process.crawl(spider_cls)
            # 开始进程
            self.process.start()
        except Exception as e:
            # 错误处理
            print(f"Error running spider: {e}")
            raise

    def add_spider(self, spider_cls):
        """添加爬虫到进程"""
        try:
            # 将爬虫添加到进程
            self.process.crawl(spider_cls)
        except Exception as e:
            # 错误处理
            print(f"Error adding spider: {e}")
            raise

# 示例用法
if __name__ == '__main__':
    # 创建进程管理器实例
    process_manager = ProcessManager()

    # 假设有一个名为ExampleSpider的Scrapy爬虫
    from example_spider import ExampleSpider
    process_manager.add_spider(ExampleSpider)
    # 运行爬虫
    process_manager.run_spider(ExampleSpider)