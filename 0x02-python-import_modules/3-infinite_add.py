#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    s = len(argv) - 1
    res = 0
    for i in range(1, s + 1):
        res += int(argv[i])
    print("{}".format(res))
