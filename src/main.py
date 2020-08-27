# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-08-26

import config
from util import PrintLog
from valid_proxy_inspector import VaildProxyInspector
from proxy_crawler import Crawler

if __name__ == '__main__':
    result_list = list()
    vaild_proxy_inspector = VaildProxyInspector(config.test_url,
                                                config.timeout)
    crawler = Crawler(config.timeout)

    for i in range(1, 10):
        proxy_list = crawler.crawl_proxy_list(start_page_id=i, page_size=1)
        if proxy_list:
            PrintLog("成功抓取%s个代理." % len(proxy_list))
            tmp = vaild_proxy_inspector.check_list(proxy_list)
            result_list.extend(tmp)
            PrintLog("当前共有%s个可用的代理" % len(result_list))
