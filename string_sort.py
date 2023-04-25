# Author: Justin Huang
# GitHub username: huangjus
# Date: 4/25/23
# Description: This code sorts a list of strings in ascending order, ignoring case. It uses the insertion sort
# algorithm and compares each element to the previous ones. If an element is smaller, it moves it to the correct
# position by swapping it with the previous element. The function converts strings to lowercase before comparing them
# using lower(), so sorting is case-insensitive.

def string_sort(a_list):
    """
    Sorts a_list of strings in ascending order, ignoring case.
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos].lower() > value.lower():
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value
