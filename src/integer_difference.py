"""Integer Difference, CodeWars Kata, level 7."""


def integer_diff(arr, n):
    """Return number of times integer difference, n, occurs within array.

    input = two parameters, a list of integers
                            an integer, n, which equals difference
    output = integer, number of times, n achieved in list
    ex: int_diff([1, 1, 5, 6, 9, 16, 27], 4) # 3 ([1, 5], [1, 5], [5, 9])
    """
    count = 0
    arr_copy = arr[::]
    for el in arr:
        for idx in range(len(arr_copy) - 1):
            if abs(el - arr_copy[idx + 1]) == n:
                count += 1
        arr_copy.pop(0)
    return count


def int_diff_one(arr, n):
    """Solution of PatrickJFiero on Codewars."""
    count = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if(abs(arr[i] - arr[j]) == n):
                count += 1
    return count


def int_diff_two(arr, n):
    """Solution of Luisho5 on Codewars."""
    r = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == n:
                r += 1
    return r
