#!/usr/bin/python3

for i in range(1, 101):
    if i < 100:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
        