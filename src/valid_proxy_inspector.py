# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-08-12

import requests

import config
from util import PrintLog, HeadersBuilder


class VaildProxyInspector(object):
    def __init__(self, url, timeout):
        self.test_url = url
        self.timeout = timeout
        self.headers_builder = HeadersBuilder()

    def check(self, ip, post):
        headers = self.headers_builder.build()
        proxies = {'http': 'http://%s:%s' % (ip, post)}
        try:
            r = requests.get(self.test_url, headers=headers,
                             proxies=proxies, timeout=self.timeout)
            if r.status_code == 200:
                return True
        except Exception:
            return False


if __name__ == '__main__':
    vaild_proxy_inspector = VaildProxyInspector(config.test_url,
                                                config.timeout)
    ip = '104.129.205.41'
    post = '10605'

    PrintLog("Start check the proxy IP: %s, POST:%s" % (ip, post))
    result = vaild_proxy_inspector.check(ip, post)
    if result:
        PrintLog("The proxy is available.")
    else:
        PrintLog("The proxy is not available.")
