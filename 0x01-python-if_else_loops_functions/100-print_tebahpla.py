#!/usr/bin/python3
for num in range(-90, -64):
    nwnum = num * -1
    if nwnum % 2 == 0:
        print("{}".format(chr(nwnum + 32)), end="")
    else:
        print("{}".format(chr(nwnum)), end="")
