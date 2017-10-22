"""Kata: Find the Odd Integer - Need to find the one odd numbered integer in a list.

#1 Best Practices Solution by cerealdinner et al.

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i"""

def find_it(seq):
    """function finds the integer that has the odd number of values once collected into a dictionary."""
    counter = {}
    for item in seq:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    for item in counter:
        if counter[item] % 2 != 0:
            return item