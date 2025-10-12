# 代码生成时间: 2025-10-13 03:45:17
import scrapy
def load_balance(url_list):
    """
    负载均衡器功能实现。
    
    :param url_list: 待请求的URL列表。
    :return: 根据负载均衡策略选择的URL。
    """
    # 检查输入列表是否为空
    if not url_list:
        raise ValueError("URL列表不能为空。")
    
    # 这里可以添加更多的负载均衡逻辑，例如轮询、随机选择等
    # 简单的轮询策略作为示例
    return url_list[0]  # 返回列表中的第一个URL

# 测试代码
if __name__ == '__main__':
    url_list = ["http://example.com/api/1", "http://example.com/api/2"]
    try:
        selected_url = load_balance(url_list)
        print("选择的URL是: ", selected_url)
    except ValueError as e:
        print(e)
        