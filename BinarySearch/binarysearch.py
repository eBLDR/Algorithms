"""
BINARY SEARCH ALGORITHM

Finds a value in a sorted data.

Halves the data, will take a maximum of log2 n + 1 rounded up
attempts, where n is the number of values in the data.

1. Let min=1 and max=n.
2. Compute guess as the average of max and min, rounded down so that it is an integer.
3. If the guess is equal to the number, stop. Return guess.
4. If the guess was too low, set min to be one larger than the guess.
5. If the guess was too high, set max to be one smaller than the guess.
6. Go back to step two.
"""

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23,
          29, 31, 37, 41, 43, 47, 53, 59,
          61, 67, 71, 73, 79, 83, 89, 97]


def get_value():
    return int(input('Is prime? (<100): '))


def binary_search(data, target):
    """ Return 1 if target is in data, -1 otherwise. """
    assert target < 100
    min_ = 0
    max_ = len(data) - 1
    while max_ >= min_:
        search = (max_ + min_) // 2  # rounded down to integer
        if data[search] == target:
            return 1
        elif data[search] < target:
            min_ = search + 1
        elif data[search] > target:
            max_ = search - 1
        print(min_, max_)
    else:
        return -1


VALUE = get_value()

result = binary_search(PRIMES, VALUE)
if result == 1:
    print('{} is prime.'.format(VALUE))
elif result == -1:
    print('{} is not prime.'.format(VALUE))
