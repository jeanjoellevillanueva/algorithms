"""
An example of `Bubble Sort Algorithm`.
"""


NUMBERS = [7, 12, 9, 11, 3]
# Output: [3, 7, 9, 11, 12]


def is_sorted(numbers):
    """
    Function to determine if the list is already sorted from lowest to highest.
    """
    for idx in range(0, len(numbers) - 1):
        if numbers[idx] > numbers[idx + 1]:
            return False
    return True


def bubble_sort(numbers):
    """
    Function to sort the list from lowest to highest.
    """
    while is_sorted(numbers) == False:
        for idx in range(0, len(numbers) - 1):
            left_number = numbers[idx]
            right_number = numbers[idx + 1]
            if left_number > right_number:
                # Sample: 12 > 9
                numbers[idx] = right_number
                numbers[idx + 1] = left_number
    return numbers


if __name__ == '__main__':
    print(bubble_sort(NUMBERS))
