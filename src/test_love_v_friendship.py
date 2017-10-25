"""Tests the love vs friendship kata."""
import pytest

FIND_PARAMS = [('attitude', 100), ('friends', 75), ('family', 66), ('bill', 35)]

@pytest.mark.parametrize('n, result', FIND_PARAMS)
def test_words_to_marks(n, result):
    """Test for words_to_marks function."""
    from love_v_friendship import words_to_marks
    assert words_to_marks(n) == result