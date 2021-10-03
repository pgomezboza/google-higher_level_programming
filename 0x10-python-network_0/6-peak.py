#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers. """

    a = 0
    b = len(list_of_integers) - 1

    if len(list_of_integers) == 0:
        return(None)

    while (a < b):
        m = int((a + b) / 2)
        if list_of_integers[m] < list_of_integers[m + 1]:
            a = m + 1
        else:
            b = m

    return(list_of_integers[a])
