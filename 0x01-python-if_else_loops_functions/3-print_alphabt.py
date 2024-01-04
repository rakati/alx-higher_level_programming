#!/usr/bin/python3
for i in range(0, 26):
    if chr(ord('a') + i) not in 'qe':
        print("{}".format(chr(ord('a') + i)), end='')
