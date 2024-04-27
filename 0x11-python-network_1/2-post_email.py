#!/usr/bin/python3
'''Script file'''

from urllib import request
from urllib import parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    post_values = {'email': sys.argv[2]}
    # Encode data will create url with values in our dic
    url_encode = parse.urlencode(post_values)
    # encode url using utf-8 encoding
    post_data = url_encode.encode('utf-8')
    # make request
    req = request.Request(url, post_data)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
