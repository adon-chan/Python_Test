# coding=utf8


import sys
import requests
import re

reload(sys)
sys.setdefaultencoding('utf-8')


# 抓取代理
class GetFreeProxy(object):
    def __init__(self):
        pass

    @staticmethod
    def freeProxyFirst():
        for page in xrange(10):
            url = 'http://www.kuaidaili.com/proxylist/' + str(page)
            bs = gethtmlTree1(url)
            proxy_list = bs.xpath('.//div[@id="index_free_list"]//tbody/tr')
            for proxy in proxy_list:
                proxy = ':'.join(proxy.xpath('./td/text()')[0:2])
                yield proxy

    @staticmethod
    def freeProxySecond():
        url = 'http://www.youdaili.net/Daili/http/'
        bs = gethtmlTree1(url)
        url_list = bs.xpath('.//div[@class="chunlist"]//a/@href')[0]
        # print url_list
        html = requests.get(url_list).content
        # print html
        proxy_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html)
        # print proxy_list
        for proxy in proxy_list:
            yield proxy


# 抓取页面内容
def gethtmlTree1(url):
    from bs4 import BeautifulSoup
    from lxml import etree
    import requests
    html = requests.get(url=url).content
    # return BeautifulSoup(html,'lxml')
    return etree.HTML(html)




# 测试抓取代理是否正常,并写入txt
# ProxyFirst = GetFreeProxy.freeProxyFirst()
# with open('E:\Github code\Python_Test\Project\Proxy\data.txt','w') as f:
#     for first in ProxyFirst:
#         code = TestProxy(first)
#         print str(first) + '---' + str(code)
#         if code==200:
#             f.write(first)
#             f.write('\n')
#
#
#     ProxySecond = GetFreeProxy.freeProxySecond()
#     for second in ProxySecond:
#         code = TestProxy(second)
#         print second + '---' + str(code)
#         if code==200:
#             f.write(second)
#             f.write('\n')
#     f.close()
#     print "写入完成"

