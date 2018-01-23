"""Maximize_product_of_arry(array series#2), Codewars Kata, level 7."""


def max_product(li, n):
    """Return maxima(not maximum) product from a list from the set number.

    input: list of integers
    output: integer, product of given integers

    ex: maxProduct ({4,3,5} , 2) returns return 20
        since the size (k) equal 2 , then it's 5*4 = 20
    """
    std_li = sorted(li)[-n:]
    product = 1
    for num in std_li:
        product *= num
    return product
