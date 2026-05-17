#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the list using slicing
    copy = my_list[:]
    if idx >= 0 and idx < len(my_list):
        copy[idx] = element
    return copy
