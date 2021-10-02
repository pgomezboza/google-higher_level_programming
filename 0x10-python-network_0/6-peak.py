#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    lof = list_of_integers
    l = 0
    r = len(lof) - 1

    if len(lof) == 0:
        return(None)
    else:
        while (l < r):
            mid = int((l + r) / 2)
            if lof[mid] < lof[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return(lof[l])
