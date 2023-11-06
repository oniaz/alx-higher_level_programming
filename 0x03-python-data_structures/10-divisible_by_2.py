#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    if my_list:
        for i in (my_list):
            if int(i % 2) == 0:
                result.append(True)
            else:
                result.append(False)
    return result
