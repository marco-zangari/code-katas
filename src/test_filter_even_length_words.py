"""Tests the filter even length words kata."""
import pytest

FIND_PARAMS = [(["Hello", "World"],[]), (["One", "Two", "Three", "Four"],["Four"]), (["Bob", "Rhino", "Paul"], ["Paul"])]

@pytest.mark.parametrize('n, result', FIND_PARAMS)
def test_find_it(n, result):
	"""Test for find_it function."""
	from filter_even_length_words import filter_even_length_words
	assert filter_even_length_words(n) == result