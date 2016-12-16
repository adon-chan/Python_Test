#coding=utf8

from Proxy.ProxyGet.ProxyGet import GetFreeProxy
import  requests
#自动获取
def refresh():
    proxy_agent={'freeProxyFirst ','freeProxySecond'}
    for proxyGetter in proxy_agent:
        with open('E:\Github code\Python_Test\Project\Proxy\data.txt','w') as f:
            for proxy in getattr(GetFreeProxy, proxyGetter.strip())():
                code = TestProxy(proxy)
                print str(proxy) + '---' + str(code)
                if code==200:
                    f.write(proxy)
                    # f.write('\n')
            f.close()
            print "写入完成"

# 测试代理是否可用
def TestProxy(proxy):
    url = 'http://www.baidu.com'
    proxy = {
             'https': proxy
            }
    html = requests.get(url, proxies=proxy)
    return html.status_code



# 读取txt内的代理
def Get_all():
    with open('E:\Github code\Python_Test\Project\Proxy\data.txt','r') as f:
        proxys=f.read()
    return proxys

# refresh()
proxys=Get_all()
for proxy in proxys:
    # print proxy.strip("\n")
    Test=TestProxy(proxy)
    print Test

