# 代码生成时间: 2025-09-20 09:22:37
import json
from scrapy.exceptions import NotConfigured

"""
JSON数据格式转换器

该程序使用Python和Scrapy框架实现JSON数据格式的转换功能。
支持将输入的JSON字符串转换为不同格式的JSON数据。
"""

class JsonDataConverter:
    def __init__(self, input_json):
        """
        初始化JsonDataConverter类

        :param input_json: 输入的JSON字符串
        """
        self.input_json = input_json

    def convert_to_pretty_json(self):
        """
        将输入的JSON字符串转换为格式化的JSON字符串

        :return: 格式化的JSON字符串
        """
        try:
            data = json.loads(self.input_json)
            return json.dumps(data, indent=4, ensure_ascii=False)
        except json.JSONDecodeError as e:
            raise NotConfigured(f"输入的JSON字符串格式不正确: {e}")

    def convert_to_compact_json(self):
        """
        将输入的JSON字符串转换为压缩的JSON字符串

        :return: 压缩的JSON字符串
        """
        try:
            data = json.loads(self.input_json)
            return json.dumps(data)
        except json.JSONDecodeError as e:
            raise NotConfigured(f"输入的JSON字符串格式不正确: {e}")

# 示例用法
if __name__ == "__main__":
    input_json = "{"name": "John", "age": 30}"

    converter = JsonDataConverter(input_json)
    pretty_json = converter.convert_to_pretty_json()
    compact_json = converter.convert_to_compact_json()

    print("格式化的JSON: ", pretty_json)
    print("压缩的JSON: ", compact_json)