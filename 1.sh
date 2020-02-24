#!/bin/bash
echo -e 'https://google.com\n\n' | python3 -c "__import__('crawl').crawl()"
