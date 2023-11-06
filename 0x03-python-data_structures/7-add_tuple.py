#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = (0, 0)
    for i in [tuple_a, tuple_b]:
        if i is None:
            i = (0, 0)
        if len(i) == 1:
            i = (i[0], 0)
        elif len(i) == 0:
            i = (0, 0)
        result = (result[0] + i[0], result[1] + i[1])
    return result
