#!/usr/bin/python3
def print_arguments(*argv):
    num_args = len(argv)
    print(f"Number of argument{'s' if num_args != 1 else ''}:")
    if num_args == 0:
        print("(or . if no arguments were passed)")
    else:
        for i, arg in enumerate(argv, start=1):
            print(f"{i}:", arg)

if __name__ == "__main__":
    import sys
    print_arguments(*sys.argv[1:])
