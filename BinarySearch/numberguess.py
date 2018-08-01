"""
Number guessing.
"""

from random import randint


def get_max():
    return int(input("max (int) = "))


def generate_data(n):
    data = []
    for i in range(1, n+1):
        data.append(i)

    return data


def get_value(n):
    return randint(1, n)


def linear_search(data, value):
    """ Searches record by record, the average
    # of attempts is 1/2 of total records. """
    assert value in data
    guessed = []
    for i in data:
        guessed.append(i)
        if i == value:
            return guessed


def binary_search(data, value):
    assert value in data
    guessed = []
    min_ = min(data)
    max_ = max(data)
    while True:
        guess = (max_ + min_) // 2  # rounded down to integer
        guessed.append(guess)
        if guess == value:
            return guessed
        elif guess < value:
            min_ = guess + 1
        elif guess > value:
            max_ = guess - 1


MAX = get_max()
VALUE = get_value(MAX)

print("VALUE is {}".format(VALUE))

option = input("\nL - Linear Search\nB - Binary Search\n").upper()
result = []

if option == 'L':
    result = linear_search(generate_data(MAX), VALUE)
elif option == 'B':
    result = binary_search(generate_data(MAX), VALUE)

if result:
    print("""IA required {} attempts to correctly guess.
{}""".format(len(result), result))
