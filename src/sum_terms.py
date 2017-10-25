"""
Kata: Sum of First nth Term of Series - Sum an nth series with floated value

#1 Best Practices: MMMAAANNN et al.

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
."""


def series_sum(n):
    """Sum of first nth term in series and return float value."""
    total_series = 0.00
    for x in range(n):
        total_series += 1 / (1 + (x * 3))
    total_series_decimal = ('{0:.2f}'.format(total_series))
    return total_series_decimal
