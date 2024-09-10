#!/usr/bin/python3
def uppercase(str):
    for char in str:
        code = ord(char)

        if code >= 97 and code <= 122:
            code -= 32

        print("{}".format(chr(code)), end="")
    else:
        print()
