"""Tests the simple pig latin kata."""
import pytest

FIND_PARAMS = [('Pig latin is cool','igPay atinlay siay oolcay'), ('This is my string','hisTay siay ymay tringsay'), ('Acta est fabula', 'ctaAay steay abulafay'), ('talia est iacta', 'aliatay steay actaiay')]

@pytest.mark.parametrize('n, result', FIND_PARAMS)
def test_pig_it(n, result):
	"""Test for find_it function."""
	from simple_pig_latin import pig_it
	assert pig_it(n) == result