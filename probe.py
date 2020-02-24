#!/usr/bin/python3
'''
todo: 
    -https
    -другие протоколы? это как бы WEB app hp, но у ftp есть дефолт веб-интерфейс => ftp-веб?
    -сохранять запросы(?оптимизация?) сразу в бд
'''
import requests
from xml.dom import minidom
from html.parser import HTMLParser
from parsehtml import parse

def crawl_urls(*urls, maxdepth = -1, debug = 0):
    '''
    Searches all SRC/HREF urls on page, recursively inspects each new layer of links starting on ones inputed in function.
    Usage: crawl_urls('http://google.com', 'http://ya.ru', maxdepth=1)
        maxdepth - maximum number of layers for each of URLs in params
    '''
    allurls = []
    def crawl(*urls, maxdepth = -1, debug = 0):
        allurls.extend(urls)
        if maxdepth >= 0:
            for current_url in urls:
                if debug:
                    print("Looking", current_url)
        #        continue
                response = requests.get(current_url)
                if response.status_code == 200:
                    content = response.content
                    try:
                        content = content.decode("utf-8")
                    except Exception as e:
                        if debug:
                            print(e)
                        continue
                    response_urls = parse(content)
                    for id, url in enumerate(response_urls):
                        if url.startswith('//'):
                            response_urls[id] = 'http:' + url
                        elif url.startswith('/'):
                            response_urls[id] = current_url + url
                    crawl(*response_urls, maxdepth = maxdepth - 1, debug = debug)
    crawl(*urls, maxdepth = maxdepth, debug = debug)
    return allurls

if __name__=='__main__':
    crawl_urls("http://ya.ru","http://google.com",maxdepth = 1)
