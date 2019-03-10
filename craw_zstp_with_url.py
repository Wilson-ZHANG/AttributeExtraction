# -*-coding:utf-8-*-

import urllib.request
import random
import requests
from bs4 import BeautifulSoup




url = "http://zstp.pcl.ac.cn:5050/trees?name=tree"
filename1 = 'zstp_tree.json'
save = open(filename1, 'a+', encoding='utf-8')
#print("title,content",file=save)
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]


def get_content(url, headers):
    '''
    @获取403禁止访问的网页
    '''
    randdom_header = random.choice(headers)

    req = urllib.request.Request(url)
    req.add_header("User-Agent", randdom_header)
    req.add_header("Host", "blog.csdn.net")
    req.add_header("Referer", "http://blog.csdn.net/")
    req.add_header("GET", url)

    content = urllib.request.urlopen(req).read()
    return content

def print_title_and_content(url):
    html = (get_content(url, my_headers)).decode()
    soup = BeautifulSoup(html, "lxml")
   # news_text = soup.find('div',class_='detail')
    #title = news_text.find('h1').get_text()
   # content = news_text.find('div').get_text()
    print(html,file=save)


def print_content_for_sentiment(url):
    html = (get_content(url, my_headers)).decode()
    soup = BeautifulSoup(html, "lxml")
    news_text = soup.find('div',class_='detail')
    title = news_text.find('h1').get_text()
    content = news_text.find('div').get_text()
    print("'"+content+"',",file=save)

def transform(filename):
    li = []
    with open(filename,'r',encoding='utf-8') as f:
        cool = f.readlines()
        for element in cool:
            li.append(element)
    return li
def main():
     url = "http://zstp.pcl.ac.cn:5050/trees?name=tree"
     print_title_and_content(url)


if __name__ == '__main__':
    main()