#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    length = len(a_dictionary)
    for i in range(length):
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                length -= 1
                break
    return a_dictionary
