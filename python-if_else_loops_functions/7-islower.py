#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
print("a is {}".format("lower" if islower("a") else "upper"))