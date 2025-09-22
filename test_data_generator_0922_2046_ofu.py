# 代码生成时间: 2025-09-22 20:46:51
import json
import random
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider

# 测试数据生成器
class TestDataGenerator:
    """用于生成测试数据的类"""
    
    def __init__(self):
        self.data = []
    
    def generate_data(self, num_items):
        """生成指定数量的测试数据
        
        :param num_items: 要生成的数据项数量
        """
        for i in range(num_items):
            self.data.append({
                'id': i,
                'name': f'User_{i}',
                'email': f'user{i}@example.com',
                'age': random.randint(18, 60),
                'city': random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'])
            })
    
    def save_data(self, file_name):
        """将生成的数据保存到JSON文件
        
        :param file_name: 要保存的文件名
        """
        try:
            with open(file_name, 'w') as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            print(f"Error saving data to file: {e}")
    
    def print_data(self):
        "