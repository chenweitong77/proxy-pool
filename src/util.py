# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-08-12

import datetime
import random

import config


# 打印日志函数
def PrintLog(log_str):
    time_ = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('[%s] %s' % (time_, log_str))


# 创建请求Headers
# Usage:
# headers_builder = HeadersBuilder()
# headers = headers_builder.build()
class HeadersBuilder(object):
    def __init__(self):
        self.user_agents = config.user_agents

    def build(self):
        headers = dict()
        idx = random.randint(0, len(self.user_agents) - 1)
        headers['User-Agent'] = self.user_agents[idx]
        return headers


# 文件管理，读写文件
class FileController(object):
    def read_file_with_split(self,
                             file_path,
                             split_str='\t',
                             split_size=None,
                             max_split_size=None,
                             min_split_size=None):
        result_list = list()
        with open(file_path) as stream:
            for line in stream:
                fields = line.strip().split(split_str)
                if split_size and len(fields) != split_size:
                    continue
                elif max_split_size and len(fields) > max_split_size:
                    continue
                elif min_split_size and len(fields) < min_split_size:
                    continue
                result_list.append(fields)
        return result_list

    def write_list_to_file(self, output_list, file_path, split_str='\t'):
        exist_list = list()
        with open(file_path, 'w+') as f:
            for sub_list in output_list:
                if sub_list in exist_list:
                    continue

                output_str = split_str.join(sub_list)
                output_str += "\n"
                f.write(output_str)
                exist_list.append(sub_list)
