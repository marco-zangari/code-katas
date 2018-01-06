"""Proper parenthetics."""


def lisp_parens_with_count(parens):
    """Output with count to see whether parens are open(1), broken(-1), or balanced(0)."""
    open_count = 0
    for par in parens:
        if par == '(':
            open_count
        elif par == ')':
            open_count -= 1
        if open_count < 0:
            return -1
    if open_count == 0:
        return 0
    else:
        return 1


def lisp_parens_with_stack(parens):
    """Output with stack to see whether parens are open(1), broken(-1), or balanced(0)."""
    open_stack = []
    for par in parens:
        if par == '(':
            open_stack.append(par)
        if par == ')':
            try:
                open_stack.pop()
            except IndexError:
                return -1
    if open_stack:
        return 1
    else:
        return 0
