#!/usr/bin/python3
def remove_char_at(string, index):
    if index < 0 or index >= len(string):
        return string

    result = ""
    for i in range(len(string)):
        if i != index:
            result += string[i]

    return result
