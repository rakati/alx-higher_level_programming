#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = dir(hidden_4)
    names.sort()
    for e in names:
        if not e.startswith('__'):
            print("{}".format(e))
