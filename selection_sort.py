"""
An example of `Selection Sort Algorithm`.
"""


NUMBERS = [7, 12, 9, 11, 3]
# Output: [3, 7, 9, 11, 12]


def selection_sort(numbers:list):
    """
    Sort the array of integers from low to highest.
    """
    sorted_array = []
    while len(numbers) != 0:
        min_number = min(numbers)
        idx = numbers.index(min_number)
        sorted_array.append(numbers.pop(idx))
    return sorted_array


if __name__ == '__main__':
    sorted_list = selection_sort(NUMBERS)
    print(sorted_list)
