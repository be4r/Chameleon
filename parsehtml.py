#!/usr/bin/python3
from html.parser import HTMLParser

srctags = ['a', 'script','iframe','img']

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        links = [] #links from this tag
        if tag in srctags:
            attr_dict = dict(attrs)
            if 'src' in attr_dict:
                links.append(attr_dict['src'])
            if 'href' in attr_dict:
                links.append(attr_dict['href'])
            for i in links:
                if i not in self.links and not i.startswith('#'):
                    if not i.startswith('about'):
                        self.links.append(i)

    def getLinks(self):
        t = self.links
        return t

def parse(html):
    p = Parser()
    try:
        p.feed(html)
        return p.getLinks()
    except Exception as e:
        print("CAN NOT PARSE!", e)
        return []
