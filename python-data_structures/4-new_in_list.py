#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list2 = my_list.copy()
    if idx < 0:
        return list2
    elif idx >= len(my_list):
        return list2
    else:
        list2[idx] = element
        return list2
