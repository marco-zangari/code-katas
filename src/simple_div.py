"""Simple Division, Kata Codewars, level 6."""


def simple_division(a, b):
    """Return True if all prime factors of b divide evenly into a.

    input = integers, two parameters, a and b
    output = bool, True or False
    ex = solve(15, 12) should equal False 15 not divisible by 2,
        i.e. 2, 3 prime factors
    """
    primes = find_prime(b)
    factors = find_factors(b)
    res = []
    for factor in factors:
        if factor in primes:
            res.append(factor)
    for el in res:
        if a % el != 0:
            return False
        else:
            return True


def find_prime(a):
    """Find prime numbers."""
    res = []
    for num in range(2, a):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            res.append(num)
    return set(res)


def find_factors(b):
    """Find factors of a number."""
    res = []
    for i in range(1, b + 1):
        if b % i == 0:
            print(i)
            res.append(i)
    return res
