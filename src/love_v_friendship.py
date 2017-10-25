"""Kata: Love vs Friendship - Place values on alphabet and sum the words

#1 Best Practices Solution acaccia et al.

def words_to_marks(s):
  return sum(ord(c)-96 for c in s)
."""

import string

def words_to_marks(s):
    """Turns words to values."""
    num = 0
    value = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        value[letter] = index + 1
    for item in s:
        num = num + value[item]
    return num