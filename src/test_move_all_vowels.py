"""Testing Move All the Vowels Series"""
import pytest

FIND_PARAMS = [('day', 'dya'), ('apple', 'pplae'), ('peace', 'pceae'), ('pax', 'pxa'), ('please', 'plseae')]

@pytest.mark.parametrize('n, result', FIND_PARAMS)
def test_move_vowels(n, result):
	"""tests move the vowels works."""
	from move_all_vowels import move_vowels
	assert move_vowels(n) == result