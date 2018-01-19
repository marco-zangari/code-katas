"""Remove Smallets, CodeWars kata, level 7."""


def remove_smallest(nums):
    """Remove smallest integer from list of integers.

    input = integers, in list
    output = integers, in list, missing the smallest value
    ex. ([1,2,3,4,5]) = [2,3,4,5]
    ex. ([5,3,2,1,4]) = [5,3,2,4]
    ex. ([2,2,1,2,1]) = [2,2,2,1]
    """
    if bool(nums) is False:
        return []

