"""
INSERTION SORT ALGORITHM

Sorts data.

1. Compares element at index 1 with elements on its left to determine how many
elements must be slid to the right.
2. Inserts the element at index 1 in the right position in the sorted subarray on the left
side of element at index 1.
3. Compares element at index 2 with elements on its left to determine how many
elements must be slid to the right.
4. Inserts the element at index 2 in the right position in the sorted subarray on the left
side of element at index 2.
5. Repeat the process until it reaches the element at second last index.
"""

from random import randint


def generate_data(n):
    data_ = []
    for i in range(n):
        data_.append(randint(1, 100))

    return data_


def insert(array, index):
    value = array[index]
    for i in range(index, 0, -1):
        if value < array[i - 1]:
            array[i] = array[i - 1]
        else:
            array[i] = value
            break
    else:
        array[0] = value


def insertion_sort(array):
    for i in range(1, len(array)):
        insert(array, i)


def insertion_sort_2(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1
        array[position] = current_value


data = generate_data(25)
print(data)
insertion_sort(data)
print(data)
