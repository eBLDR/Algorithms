"""
SELECTION SORT ALGORITHM

Sorts data.

1. Find the smallest element in the array, swap it with the first element.
2. Find the second-smallest element, this time searching only in a subarray
from second element to the end, swap it with the second element.
3. Repeat finding the next-smallest element, and swapping it into the
correct position until the data is sorted.
"""

from random import randint


def generate_data(n):
    data = []
    for i in range(n):
        data.append(randint(1, 100))

    return data


def swap(array, index_1, index_2):
    """ Swap index 1 for index 2. """
    tmp = array[index_1]
    array[index_1] = array[index_2]
    array[index_2] = tmp


def find_index_of_minimum(array, start_index):
    """ Returns the index of the smallest value in subarray (array[start_index:]). """
    min_index = start_index
    for i in range(start_index, len(array)):
        if array[i] < array[min_index]:
            min_index = i

    return min_index


def selection_sort(array):
    for i in range(len(array)):
        swap(array, i, find_index_of_minimum(array, i))


data = generate_data(25)
print(data)
selection_sort(data)
print(data)
