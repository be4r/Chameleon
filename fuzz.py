#!/usr/bin/python3
from crawl import crawl
import dbinit
import requests


def fuzz():
    with dbinit.connection as cur:
        cur.execute("SELECT url FROM urls")
        urls = cur.fetchall()
        for i in urls:
            print(i[0])
            continue
            cookies = {}
            params = {}
            headers = {}
            #allow_redirects = True
            #files = {'file': ('filename', open('filename'))}
            #data = json.dumps({})
            #use session?

            requests.get(i)
            requests.post(i)
            requests.delete(i)
            requests.put(i)
            requests.patch(i)
            requests.head(i)
            requests.options(i)
#            requests.trace()
#            requests.connect()
#            requests.path()

        print("\n".join(str(i) for i in urls))


fuzz()



