"""Tests the reversed strings kata."""
import pytest

FIND_PARAMS = [('world', 'dlrow'), ('hello', 'olleh'), ('', ''), ('harry', 'yrrah')]

@pytest.mark.parametrize('n, result', FIND_PARAMS)
def test_reversed_strings(n, result):
	"""test function for solution."""
	from reversed_strings import solution
	assert solution(n) = result