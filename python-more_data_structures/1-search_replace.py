#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) >= 0:
        new_list = my_list[:]
        new_list[search] = replace
    return new_list
