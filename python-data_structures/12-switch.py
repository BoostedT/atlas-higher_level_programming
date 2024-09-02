#!/usr/bin/python3
def switch(my_list=[]):
    if len(my_list) == 0:
        return (None)

    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(False)
        else:
            new_list.append(True)

    return (new_list)
