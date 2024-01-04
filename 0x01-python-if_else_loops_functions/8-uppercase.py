#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            print("{}".format(chr(ord('A') + ord(c) - ord('a'))), end='')
        else:
            print("{}".format(c), end='')
    print()
