#!/usr/bin/python3
'''Script file'''

from urllib import request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with request.urlopen(url) as resp:
        print(resp.headers.get('X-Request-Id'))
