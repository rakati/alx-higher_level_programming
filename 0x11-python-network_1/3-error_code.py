#!/usr/bin/python3
'''Script file'''

from urllib import request
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
