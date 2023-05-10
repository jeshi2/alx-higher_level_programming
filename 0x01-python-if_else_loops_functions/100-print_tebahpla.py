#!/usr/bin/python3
output = ""
for i in range(122, 96, -1):
    output += "{0}{1}".format(chr(i), chr(i - 33) if i > 97 else "")

print(output)

