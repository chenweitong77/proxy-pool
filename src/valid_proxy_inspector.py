# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-08-12

import os

import config
from util import PrintLog, HeadersBuilder

class VaildProxyInspector(object):
    def __init__(self, url):
        self.test_url = url

    def check(self, ip, post):
        headers_builder = HeadersBuilder()
        headers = headers_builder.build()
        print(headers)
        return False

if __name__ == '__main__':
    vaild_proxy_inspector = VaildProxyInspector(config.test_url)
    ip = '104.129.205.46'
    post = '10605'

    PrintLog("Start check the proxy IP: %s, POST:%s" % (ip, post))
    result = vaild_proxy_inspector.check(ip, post)
    if result:
        PrintLog("The proxy is available.")
    else:
        PrintLog("The proxy is not available.")