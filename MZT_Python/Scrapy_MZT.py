#coding=utf8
import requests
from bs4 import BeautifulSoup
import thread
import time

url='http://jandan.net/ooxx'
page=requests.get(url)
contents=page.text
# print contents
soup=BeautifulSoup(contents,'lxml')

# 取出爬取页面的最大值
num=soup.find('span',class_='current-comment-page').text.strip("[]")
max_num=int(num)
# print type(max_num)

def Get_URL(id):
    page=requests.get('http://jandan.net/ooxx/page-'+str(id)+'#comments')
    # page=requests.get(url)
    contents=page.text
# print(contents)
    soup=BeautifulSoup(contents,'lxml')
    links=soup.find_all('a',class_='view_img_link')

    # 将URL写入本地文件
    with open('E:\\test\\MZT_Python\\data\\url_addr.txt','a') as f:
        for link in links:
        # print(link.get('href'))
            addr=link.get('href')
            print(addr)
            f.write(addr)
            f.write('\n')
    f.close()

# for id in xrange(max_num):
#     Get_URL(id)

# 引入线程
# 为线程定义一个函数

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < max_num:
      time.sleep(delay)
      count += 1
      Get_URL(count)
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# 创建两个线程
try:
   thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   thread.start_new_thread( print_time, ("Thread-2", 1, ) )
   thread.start_new_thread( print_time, ("Thread-3", 1, ) )
   thread.start_new_thread( print_time, ("Thread-4", 1, ) )

except:
   print "Error: unable to start thread"

while 1:
   pass







