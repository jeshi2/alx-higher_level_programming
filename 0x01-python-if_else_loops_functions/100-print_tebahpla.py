#!/usr/bin/python3
output = ""
for i in range(122, 96, -1):
    output += "{}{}".format(chr(i), chr(i - 32) if i > 97 else "")
print(output)
