#!/usr/bin/env python
# encoding: utf-8

import urllib2, base64
from time import sleep

router_url = 'http://192.168.1.1/'
username = 'admin'
password = 'admin'

base64string = base64.encodestring('%s:%s' % (username,password))[:-1]


def dialUp():
    """dial up"""
    dial_up_url = router_url + 'userRpm/StatusRpm.htm?Connect=%C1%AC%20%BD%D3&wan=1'

    headers = {
            'Connection': 'keep-alive',
            'Authorization':  "Basic %s" % base64string,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': router_url + 'userRpm/StatusRpm.htm',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3'
    }


    request = urllib2.Request(
                url = dial_up_url,
                headers = headers)

    response = urllib2.urlopen(request, timeout = 10)


def dialDown():
    """dial down"""
    dial_down_url = router_url + 'userRpm/StatusRpm.htm?Disconnect=%B6%CF%20%CF%DF&wan=1'

    headers = {
            'Connection': 'keep-alive',
            'Authorization':  "Basic %s" % base64string,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': router_url + 'userRpm/StatusRpm.htm',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3'
    }


    request = urllib2.Request(
                url = dial_down_url,
                headers = headers)

    response = urllib2.urlopen(request, timeout = 10)



if __name__ == '__main__':
    dialDown()
    sleep(10)
    dialUp()


