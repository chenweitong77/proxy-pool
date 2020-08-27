# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-08-26

import re
import requests
import time

import config
from util import PrintLog, HeadersBuilder


class Crawler(object):
    def __init__(self, timeout):
        self.timeout = timeout
        self.headers_builder = HeadersBuilder()

    def html(self, url):
        headers = self.headers_builder.build()
        try:
            r = requests.get(url, headers=headers, timeout=self.timeout)
            PrintLog("访问成功：%s" % url)
            if r.status_code == 200:
                return r.text
        except Exception:
            PrintLog("无法访问：%s，请确保网络畅通后重试！" % url)
            return False

    def crawl_kuaidaili(self, start_page_id=1, page_size=3):
        proxy_list = list()
        for page in range(start_page_id, page_size + start_page_id):
            # 国内高匿代理
            start_url = 'https://www.kuaidaili.com/free/inha/%s' % page
            html = self.html(start_url)
            if not html:
                return proxy_list

            ip_adress = re.compile(config.regex_dict['kuaidaili'])
            re_ip_adress = ip_adress.findall(str(html))
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                proxy_list.append(result)

            time.sleep(1)

        return proxy_list

    def crawl_kxdaili(self, start_page_id=1, page_size=3):
        proxy_list = list()
        for page in range(start_page_id, page_size + start_page_id):
            start_url = 'http://www.kxdaili.com/dailiip/1/%s.html' % page
            html = self.html(start_url)
            if not html:
                return proxy_list

            ip_adress = re.compile(config.regex_dict['kxdaili'])
            re_ip_adress = ip_adress.findall(str(html))
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                proxy_list.append(result)

            time.sleep(1)

        return proxy_list

    def crawl_proxy_list(self, start_page_id=1, page_size=3):
        result_list = list()
        proxy_list = self.crawl_kuaidaili(start_page_id=start_page_id,
                                          page_size=page_size)
        result_list.extend(proxy_list)
        proxy_list = self.crawl_kxdaili(start_page_id=start_page_id,
                                        page_size=page_size)
        result_list.extend(proxy_list)
        return result_list


if __name__ == '__main__':
    c = Crawler(config.timeout)
    proxy_list = c.crawl_proxy_list()
    if proxy_list:
        PrintLog("成功抓取%s个代理." % len(proxy_list))
