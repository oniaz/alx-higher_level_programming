#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key in a_dictionary.keys():
            max_key = key
            break
        for key in a_dictionary.keys():
            if a_dictionary[key] > a_dictionary[max_key]:
                max_key = key
        return max_key
