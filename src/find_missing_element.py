"""Find missing element between two arrays, CodeWars Kata, level 7."""


def missing(arr1, arr2):
    """Return missing element in arr2 that was in arr1.

    input = two arrays with integers
    output = one integer, i.e. the missing element from arr1
    ex. [6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2] should return 8
    ex. [1, 2, 2, 3], [1, 2, 3] should return 2
    nice solution: return sum(arr1) - sum(arr2)

    """
    one = sorted(arr1)
    two = sorted(arr2)
    if one[-1] not in two or one[-1] == 0:
        return one[-1]
    if len(one) == 1:
        return one[0]
    for idx, num in enumerate(two):
        if one[idx] != two[idx]:
            return one[idx]
