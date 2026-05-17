#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0
    argc = len(argv)
    if argc == 1:
        print("0")
    else:
        for i in range(1, argc):
            total += int(argv[i])
        print("{}".format(total))
