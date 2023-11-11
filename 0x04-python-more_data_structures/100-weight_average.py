#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    if not my_list:
        return result
    sum_scoreWeight = sum(x for x in list(map(lambda x: x[0] * x[1], my_list)))
    sum_weight = sum(x for x in list(map(lambda x: x[1], my_list)))
    res = sum_scoreWeight/sum_weight
    return res
