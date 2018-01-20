"""Sectional Array Sort, CodeWars kata, level 7."""


def sect_sort(arr, start, length=0):
    """Return sort from given position in ascending order.

    documentation: sect_sort(array, start, length)
    array: array to sort
    start: staring position
    length: number of items to sortoptional
    input = list of integers
    output = list of integers, sorted in ascending order
    ex. sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 2) //=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ex. sect_sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5) //=> [9, 7, 1, 2, 3, 4, 5, 8, 6]
    """
    if not arr:
        return arr
    if length == 0:
        pre = arr[:start]
        return prestart + sorted(arr[start:])
    if length > 0:
        pre = arr[:start]
        mid = sorted(arr[start: start + length])
        post = arr[start + length:]
        return pre + mid + post
