import requests
from bs4 import BeautifulSoup

# url='http://jandan.net/ooxx/page-2238#comments'
def Get_URL(id):
    page=requests.get('http://jandan.net/ooxx/page-'+str(id)+'#comments')
    # page=requests.get(url)
    contents=page.text
# print(contents)
    soup=BeautifulSoup(contents,'lxml')
    links=soup.find_all('a',class_='view_img_link')
    for link in links:
    # print(link.get('href'))
        addr=link.get('href')
        print addr


for id in range(0,2239):
    Get_URL(id)



