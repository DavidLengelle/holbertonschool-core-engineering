#!/usr/bin/env python3

for i in range(9):
    for j in range(i + 1, 10):
        print("{0}{1}, ".format(i, j), end="")
print("{0}{1}".format(i, j))
