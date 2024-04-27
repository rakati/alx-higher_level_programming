#!/usr/bin/python3
'''Script file'''

import requests
from requests.exceptions import HTTPError
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except HTTPError as e:
        print("Error code:", r.status_code)
