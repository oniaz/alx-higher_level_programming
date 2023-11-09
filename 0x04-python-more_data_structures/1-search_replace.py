#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def replace_element(element):
        if element == search:
            return replace
        return element
    return list(map(replace_element, my_list))
