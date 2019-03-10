# -*-coding:utf-8-*-

import urllib.request
import random
import requests
from bs4 import BeautifulSoup
import json
import urllib.parse

url_head = "http://zstp.pcl.ac.cn:5050/knowledge?name="
filename1 = 'zstp_whole.json'
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
    print(html[:-1],file=save)


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


def extract_name(input_file):
    name_list = []
    try:
        with open(input_file, encoding='utf-8') as f:
            for line in f:
                r = json.loads(line, strict=False)
                for i in range(14613,27575):
                    try:
                        temp_name = r['nodes'][i]['name'].encode("utf-8").decode("utf-8")
                        name_list.append(temp_name)
                        # print(temp_name)
                    except:
                        pass
    except:
        pass
    return name_list
def main():

     url_head = "http://zstp.pcl.ac.cn:5050/knowledge?name="
     input_file = 'zstp_tree.json'
     name_temp = extract_name(input_file)
     #print(name_temp[0])
     #print(name_temp[1])
     #print(name_temp.__len__())
     for name_d in name_temp:
        url = url_head+urllib.parse.quote(name_d)
        print(url)
        print_title_and_content(str(url))


if __name__ == '__main__':
    main()
    #req = urllib.request.Request('http://zstp.pcl.ac.cn:5050/knowledge?name=坐珠达西')
    #content = urllib.request.urlopen(req).read()
    #print(content)