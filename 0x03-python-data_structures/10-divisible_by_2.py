#!/usr/bin/python3
"""Only by 2"""
#  function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    result = []
    for n in my_list:
        result.append(n % 2 == 0)
    return result
