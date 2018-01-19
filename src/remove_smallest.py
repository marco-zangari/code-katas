"""Remove Smallest, CodeWars kata, level 7."""


def remove_smallest(nums):
    """Remove smallest integer from list of integers.

    input = integers, in list
    output = integers, in list, missing the smallest value
    ex. [1,2,3,4,5] = [2,3,4,5]
    ex. [5,3,2,1,4] = [5,3,2,4]
    ex. [2,2,1,2,1] = [2,2,2,1]
    """
    if not nums:
        return []
    output = nums[0]
    new_nums = nums[::]
    for num in new_nums:
        if num < output:
            output = num
    # while len(new_nums) == len(nums):
    for i in range(len(new_nums)):
        if new_nums[i] == output:
            new_nums.remove(new_nums[i])
            break
    return new_nums


def remove_smallest_1(nums):
    """From Streetmentioner et al."""
    if nums:
        nums.remove(min(nums))
    return nums
