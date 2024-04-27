#!/usr/bin/python3
'''Script file'''
from urllib import request
if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        print("Body response:")
        data = resp.read()
        print("   - type:", data)
        print("   - content:", type(data))
        print("   - utf8 content:", data.decode("utf-8"))
