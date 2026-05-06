#!/usr/bin/env python3

for i in range(9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{0}{1}".format(i, j))
        else:
            print("{0}{1}, ".format(i, j), end="")
