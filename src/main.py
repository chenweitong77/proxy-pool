# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-08-26

import os

import config
from util import PrintLog, FileController
from valid_proxy_inspector import VaildProxyInspector
from proxy_crawler import Crawler

if __name__ == '__main__':
    base_path = os.path.dirname(__file__)
    proxy_file = os.path.join(base_path, 'proxy.info')
    result_list = list()
    vaild_proxy_inspector = VaildProxyInspector(config.test_url,
                                                config.timeout)
    crawler = Crawler(config.timeout)
    file_controller = FileController()

    # 读取现有代理池，删除过期代理结果.
    if os.path.exists(proxy_file):
        proxy_list = file_controller.read_file_with_split(proxy_file,
                                                          split_size=2)
        for proxy_node in proxy_list:
            ip, post = proxy_node
            if vaild_proxy_inspector.check(ip, post):
                result_list.append(proxy_node)

    # 抓取新的代理池.
    for i in range(1, config.max_page_size + 1):
        proxy_list = crawler.crawl_proxy_list(start_page_id=i, page_size=1)
        if proxy_list:
            PrintLog("成功抓取%s个代理." % len(proxy_list))
            tmp = vaild_proxy_inspector.check_list(proxy_list)
            result_list.extend(tmp)
            PrintLog("当前共有%s个可用的代理" % len(result_list))

    # 保存代理池到文件.
    file_controller.write_list_to_file(result_list, proxy_file)
