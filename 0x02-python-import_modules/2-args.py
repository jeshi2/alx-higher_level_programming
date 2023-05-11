#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    _num = len(args)

    if _num == 0:
        print("0 arguments.")

    elif _num == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(_num))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

