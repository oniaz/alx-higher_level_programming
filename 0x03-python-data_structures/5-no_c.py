#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        str = ""
        for i in my_string:
            if i != "C" and i != "c":
                str += i
        return str
