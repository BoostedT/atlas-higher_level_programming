#!/usr/bin/python3
def add_arguments(*args):
    total = 0
    for num in args:
        total += num
    return total


if __name__ == "__main__":
    import sys
    arguments = list(map(int, sys.argv[1:]))
    result = add_arguments(*arguments)
    print(result)
