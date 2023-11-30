#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cnt = len(sys.argv) - 1

    def printarg(cnt):
        for i in range(1, cnt + 1):
            print("{}: {}".format(i, sys.argv[i]))

    if cnt == 1:
        print("{} argument:".format(cnt))
        printarg(cnt)
    elif cnt == 0:
        print("{} arguments.".format(cnt))
    else:
        print("{} arguments:".format(cnt))
        printarg(cnt)
