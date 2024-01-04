#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    s = len(argv) - 1
    if s == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(s, 's' if s != 1 else ''))
        for i in range(1, s + 1):
            print("{}: {}".format(i, argv[i]))
