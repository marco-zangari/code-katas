"""Test sum nth series."""
import pytest

FIND_PARAMS = [(1, "1.00")]

@pytest.mark.parametrize('n, result', FIND_PARAMS)
def test_series_sum(n, result):
    """Test sum_series function."""
    from sum_terms import series_sum
    assert series_sum(n) == result
