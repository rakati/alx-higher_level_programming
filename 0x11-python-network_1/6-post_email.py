#!/usr/bin/python3
'''Script file'''

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, payload)
    print(r.text)
