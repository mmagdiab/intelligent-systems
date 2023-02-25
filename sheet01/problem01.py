"""
Write a Program to sort 1D array.
"""


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    left_pointer = right_pointer = index = 0
    while left_pointer < len(left_half) and right_pointer < len(right_half):
        if left_half[left_pointer] <= right_half[right_pointer]:
            array[index] = left_half[left_pointer]
            left_pointer += 1
        else:
            array[index] = right_half[right_pointer]
            right_pointer += 1
        index += 1

    # flush the remaining
    while left_pointer < len(left_half):
        array[index] = left_half[left_pointer]
        index += 1
        left_pointer += 1

    while right_pointer < len(right_half):
        array[index] = right_half[right_pointer]
        index += 1
        right_pointer += 1

    return array


print(merge_sort([64, 25, 12, 22, 11]))
