#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ =''

import urllib.request
import json
import chardet

from globalpkg.log import logger
from globalpkg.global_var import *
from unittesttestcase import MyUnittestTestCase
from httpprotocol import MyHttp

__all__ = ['InterfaceUnittestTestCase']

class InterfaceUnittestTestCase(MyUnittestTestCase):
    outputs_list = []
    def test_interface_of_urlencode(self): # 针对请求体为url编码的：b'id=1318&password=e10adc3949ba59abbe56e057f20f883e'
        headers = self.headers.copy()
        for host in global_headers:
            # 判断该host下是否有全局请求头
            host_of_interface = self.http.get_host()
            if host == host_of_interface:
               headers.update(global_headers[host])
        self.http.set_header(headers)

        method = self.method.lower()
        if method == 'post':
            logger.info('正在发起POST请求...')
            self.params = urllib.parse.urlencode(self.params)  # 将参数转为url编码字符串# 注意，此处params为字典类型的数据
            self.params = self.params.encode('utf-8')
            response = self.http.post(self.url, self.params)
        elif method == 'get':
            logger.info('正在发起GET请求...')
            self.params = urllib.parse.urlencode(self.params)
            response = self.http.get(self.url, self.params)

        encoding = chardet.detect(response[0])['encoding']
        logger.info('正在对服务器返回body进行解码')
        if  encoding == 'GB2312' or encoding == 'windows-1252' or encoding=='ISO-8859-2':
            body = response[0].decode('gbk')  # decode函数对获取的字节数据进行解码
        elif encoding == 'utf-8':
            body = response[0].decode('utf-8')
        elif encoding == 'ascii':
            body = response[0].decode('unicode_escape')
        else:
            logger.info('解码失败，未知编码:%s，不对body做任何解码' % encoding)
            body = response[0]

        header = response[1]
        code = response[2]

        logger.info('服务器返回结果"响应体(body)": %s' % body)
        logger.info('服务器返回结果"请求头(headers)": %s' % header)
        logger.info('服务器返回结果"状态码(code)": %s' % code)

        if self.expected_result == '': # 不对结果做任何处理
            self.assertEqual(1, 1, msg='测试通过')
            return

        response_to_check = (self.expected_result['检查']).lower()

        if response_to_check == 'body':
            self.assert_result(body)
            # 断言成功后，保存结果
            self.save_result(body)
        elif response_to_check == 'header':
            self.assert_result(header)
            # 断言成功后，保存结果
            self.save_result(header)
        elif response_to_check == 'code':
            self.assert_result(code)
            # 断言成功后，保存结果
            self.save_result(code)

        # 后台数据库校验
        # 新增数据库校验的代码

    def test_interface_of_json(self): # 针对请求体为json格式的：b'id=1318&password=e10adc3949ba59abbe56e057f20f883e'
            headers = self.headers.copy()
            for host in global_headers:
                # 判断该host下是否有全局请求头
                host_of_interface = self.http.get_host()
                if host == host_of_interface:
                   headers.update(global_headers[host])
            self.http.set_header(headers)

            method = self.method.lower()
            if method == 'post':
                logger.info('正在发起POST请求...')
                self.params = json.dumps(self.params)  # 将参数转为json格式字符串
                self.params = self.params.encode('utf-8')
                response = self.http.post(self.url, self.params)
            elif method == 'get':
                logger.info('正在发起GET请求...')
                self.params = urllib.parse.urlencode(self.params)
                response = self.http.get(self.url, self.params)

            encoding = chardet.detect(response[0])['encoding']
            logger.info('正在对服务器返回body进行解码')
            if encoding == 'GB2312' or encoding == 'windows-1252' or encoding=='ISO-8859-2':
                body = response[0].decode('gbk')  # decode函数对获取的字节数据进行解码
            elif encoding == 'utf-8':
                body = response[0].decode('utf-8')
            elif encoding == 'ascii':
                body = response[0].decode('unicode_escape')
            else:
                logger.info('解码失败，未知编码:%s，不对body做任何解码' % encoding)
                body = response[0]

            header = response[1]
            code = response[2]

            logger.info('服务器返回结果"响应体(body)": %s' % body)
            logger.info('服务器返回结果"请求头(headers)": %s' % header)
            logger.info('服务器返回结果"状态码(code)": %s' % code)

            if self.expected_result == '': # 不对结果做任何处理
                self.assertEqual(1, 1, msg='测试通过')
                return

            response_to_check = (self.expected_result['检查']).lower()

            if response_to_check == 'body':
                self.assert_result(body)
                # 断言成功后，保存结果
                self.save_result(body)
            elif response_to_check == 'header':
                self.assert_result(header)
                # 断言成功后，保存结果
                self.save_result(header)
            elif response_to_check == 'code':
                self.assert_result(code)
                # 断言成功后，保存结果
                self.save_result(code)

    def test_interface_of_xml(self): # 针对请求体为webservice xml格式的
            headers = self.headers.copy()
            for host in global_headers:
                # 判断该host下是否有全局请求头
                host_of_interface = self.http.get_host()
                if host == host_of_interface:
                   headers.update(global_headers[host])
            self.http.set_header(headers)

            method = self.method.lower()
            if method == 'post':
                logger.info('正在发起POST请求...')
                self.params = self.params.encode('utf-8')
                response = self.http.post(self.url, self.params)
            elif method == 'get':
                logger.info('正在发起GET请求...')
                self.params = urllib.parse.urlencode(self.params)
                response = self.http.get(self.url, self.params)

            encoding = chardet.detect(response[0])['encoding']
            logger.info('正在对服务器返回body进行解码')
            if  encoding == 'GB2312' or encoding == 'windows-1252' or encoding=='ISO-8859-2':
                body = response[0].decode('gbk')  # decode函数对获取的字节数据进行解码
            elif encoding == 'utf-8':
                body = response[0].decode('utf-8')
            elif encoding == 'ascii':
                body = response[0].decode('unicode_escape')
            else:
                logger.info('解码失败，未知编码:%s，不对body做任何解码' % encoding)
                body = response[0]

            header = response[1]
            code = response[2]

            logger.info('服务器返回结果"响应体(body)": %s' % body)
            logger.info('服务器返回结果"请求头(headers)": %s' % header)
            logger.info('服务器返回结果"状态码(code)": %s' % code)

            if self.expected_result == '': # 不对结果做任何处理
                self.assertEqual(1, 1, msg='测试通过')
                return

            response_to_check = (self.expected_result['检查']).lower()

            if response_to_check == 'body':
                self.assert_result(body)
                # 断言成功后，保存结果
                self.save_result(body)
            elif response_to_check == 'header':
                self.assert_result(header)
                # 断言成功后，保存结果
                self.save_result(header)
            elif response_to_check == 'code':
                self.assert_result(code)
                # 断言成功后，保存结果
                self.save_result(code)

    def test_interface_of_outer(self): # 外部接口
            headers = self.headers.copy()

            myhttp = MyHttp('http', 'ditu.amap.com', '80') # 注意该代码行的未知
            for host in global_headers:
                # 判断该host下是否有全局请求头
                host_of_interface = self.http.get_host()
                if host == host_of_interface:
                   headers.update(global_headers[host])
            self.http.set_header(headers)

            sql_update = 'UPDATE '+ case_step_report_tb +' SET protocol=\"%s\",host=\"%s\", port=\"%s\"' \
                             ' WHERE executed_history_id = %s and testcase_id = %s and step_id = %s'
            data = ('http', 'ditu.amap.com', '80', executed_history_id, self.testcase_id, self.step_id)
            logger.info('正在更新步骤端口，主机，协议等配置信息')
            testdb.execute_update(sql_update, data)

            method = self.method.lower()
            if method == 'post':
                logger.info('正在发起POST请求...')
                self.params = json.dumps(self.params)  # 将参数转为json格式字符串
                self.params = self.params.encode('utf-8')
                response = myhttp.post(self.url, self.params)
            elif method == 'get':
                logger.info('正在发起GET请求...')
                self.params = urllib.parse.urlencode(self.params)
                response = myhttp.get(self.url, self.params)

            logger.info('正在对服务器返回body进行解码')
            encoding = chardet.detect(response[0])['encoding']
            if encoding == 'GB2312':
                body = response[0].decode('gbk')  # decode函数对获取的字节数据进行解码
            elif encoding == 'utf-8':
                body = response[0].decode('utf-8')
            elif encoding == 'ascii':
                body = response[0].decode('unicode_escape')
            else:
                logger.info('解码失败，未知编码:%s，不对body做任何解码' % encoding)
                body = response[0]

            header = response[1]
            code = response[2]

            logger.info('服务器返回结果"响应体(body)": %s' % body)
            logger.info('服务器返回结果"请求头(headers)": %s' % header)
            logger.info('服务器返回结果"状态码(code)": %s' % code)

            if self.expected_result == '': # 不对结果做任何处理
                self.assertEqual(1, 1, msg='测试通过')
                return

            response_to_check = (self.expected_result['检查']).lower()

            if response_to_check == 'body':
                self.assert_result(body)
                # 断言成功后，保存结果
                self.save_result(body)
            elif response_to_check == 'header':
                self.assert_result(header)
                # 断言成功后，保存结果
                self.save_result(header)
            elif response_to_check == 'code':
                self.assert_result(code)
                # 断言成功后，保存结果
                self.save_result(code)