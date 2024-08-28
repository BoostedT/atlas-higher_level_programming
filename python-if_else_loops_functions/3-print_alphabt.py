#!/usr/bin/python3
def alphabet():
    for letters in range(ord('a'), ord('z') + 1):
        if chr(letters) == 'e' or chr(letters) == 'q':
            continue
        print("{:c}".format(letters), end=" ")


alphabet()
