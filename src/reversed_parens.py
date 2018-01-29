"""Simple Reversed Parentheses, Codewars Kata, level 6."""

import math


def reverse_parens(s):
    """Return count of number of reversals needed for proper parentheses.

    input: string, with open and closed parens
    output: int, number of reversals, or -1 if not possible
    ex: solve(")(") = 2
        solve("(((())") = 1
        solve("(((") = -1
    """
    l = len(s)
    if l % 2 == 1:
        return -1
    stack = []
    open_count = 0
    closed_count = 0
    for parens in s:
        if parens == '(':
            if not stack:
                stack.append(parens)
                open_count += 1
            else:
                if stack[-1] == '(':
                    stack.append(parens)
                    open_count += 1
                if stack[-1] == ')':
                    stack.append(parens)
                    open_count += 1
        if parens == ')':
            if not stack:
                stack.append(parens)
                closed_count += 1
            else:
                if stack[-1] == ')':
                    stack.append(parens)
                    closed_count += 1
                else:
                    stack.pop(-1)
                    open_count -= 1
    output = math.ceil(open_count / 2) + math.ceil(closed_count / 2)
    return output
