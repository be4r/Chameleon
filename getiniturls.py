#!/usr/bin/python3
def getiniturls():
    '''
        input: null
        output: list of urls to init
    '''
    urls = []
    while True:
        s = input()
        if not s:
            break
        urls.append(s)
    return urls
