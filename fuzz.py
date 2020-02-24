#!/usr/bin/python3
from crawl import crawl
import dbinit
import requests
'''
TODO:
    escape quotes in insert
    use keyword arguments
    ???
'''

def fuzz():
    methods = ["get", "post", "delete", "put", "patch", "head", "options"] 
    # ["trace", "connect", "path"] #not implemented in requests
    with dbinit.connection as cur:
        cur.execute("SELECT url FROM urls")
        urls = cur.fetchall()
        for url, *params in urls:
            print('urls', url)
#            continue
            cookies = {}
            headers = {}
            params = {} #get
            data = {} #body: all \ {get, head}
            #allow_redirects = False
            #files = {'file': ('filename', open('filename'))}
            #data = json.dumps({})
            #use session?
            for method in methods:
                print('Calling [', method, '] on', url)
                #form a request and then parse
                req = requests.Request(method, url, cookies = cookies,
                        params = params, headers = headers, data = data).prepare()
                req_text = ('{}\r\n{}\r\n\r\n{}'.format(req.method + ' ' + req.url, '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()), req.body or '')).rstrip()
                response = getattr(requests, method)(url, 
                        cookies = cookies, 
                        params = params, 
                        headers = headers,
                        data = data)
                ## QUOTES
                print("INSERT INTO reqs(req, cont) VALUES('"
                        + req_text +"','"
                        + response.content.decode('utf-8') + "')")
                cur.execute("INSERT INTO reqs(req, cont) VALUES('" 
                        + req_text +"','"
                        + response.content.decode('utf-8') + "')")
            '''
            requests.get(i)
            requests.post(i)
            requests.delete(i)
            requests.put(i)
            requests.patch(i)
            requests.head(i)
            requests.options(i)
            '''
#            requests.trace()
#            requests.connect()
#            requests.path()

        print("\n".join(str(i) for i in urls))


fuzz()



