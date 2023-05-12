#!/usr/bin/python3
"""Find the max"""
# function that finds the biggest integer of a list.
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_x = my_list[0]
    for n in my_list:
        if n > max_x:
            max_x = n

    return max_x
