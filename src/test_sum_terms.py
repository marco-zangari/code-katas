"""Test sum nth series."""
import pytest

FIND_PARAMS = [((1), "1.00"), ((2), "1.25"), ((3), "1.39"), ((10), "1.81"), ((11), "1.84"), ((12), "1.87"), ((13), "1.89")]

@pytest.mark.parametrize('n, result', FIND_PARAMS)
def test_series_sum(n, result):
    """Test sum_series function."""
    from sum_terms import series_sum
    assert series_sum(n) == result
