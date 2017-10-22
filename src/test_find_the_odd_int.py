"""Tests the find the odd integer kata."""
import pytest

FIND_PARAMS = [([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5], 5), ([1,1,2,-2,5,2,4,4,-1,-2,5], -1), ([20,1,1,2,2,3,3,5,5,4,20,4,5], 5), ([10], 10)]

@pytest.mark.parametrize('n, result', FIND_PARAMS)
def test_find_it(n, result):
	"""Test for find_it function."""
	from find_the_odd_int import find_it
	assert find_it(n) == result