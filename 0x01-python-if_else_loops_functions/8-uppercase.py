#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            m = chr(ord('A') + ord(c) - ord('a'))
        else:
            m = c
        print("{}".format(m), end='')
    print()
