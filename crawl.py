#!/usr/bin/python3
from getiniturls import getiniturls
from probe import crawl_urls
#import dbinit
import pymysql


def crawl():
    urls = crawl_urls(*getiniturls(), maxdepth=1)
    connection = pymysql.connect('localhost', 'usser', 'P4$sW0rD!1', 'reqs')
    print(connection, type(connection))
    with connection:
        cur = connection.cursor()
        for i in urls:
            print("INSERT INTO urls(url) VALUES ('{}')".format(i))
            cur.execute("INSERT INTO urls(url) VALUES ('{}')".format(i))

        cur.execute("SELECT * FROM urls")
        querry_res = cur.fetchall()

        print("\n".join(str(i) for i in querry_res))
