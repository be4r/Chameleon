#!/usr/bin/python3
from getiniturls import getiniturls
from probe import crawl_urls
import dbinit


def crawl():
    urls = crawl_urls(*getiniturls(), maxdepth=1)
    with dbinit.connection as cur:
#       cur = connection.cursor()
        for i in urls:
            cur.execute("INSERT INTO urls(url) VALUES ('{}')".format(i))

        cur.execute("SELECT * FROM urls")
        querry_res = cur.fetchall()

        print("\n".join(str(i) for i in querry_res))
