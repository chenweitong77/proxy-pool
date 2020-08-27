# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-08-12

# 测试代理网址，request百度查看代理是否可用.
test_url = "http://www.baidu.com"
timeout = 3

# Headers参数池
user_agents = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
]

# 正则表达式字典
regex_dict = {
    'kuaidaili':
    '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>',
    'kxdaili': '<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>'
}
