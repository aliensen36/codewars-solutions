import pytest
from solution import alphabet_position


def test_kata_example():
    assert alphabet_position("The sunset sets at twelve o' clock.") == (
        "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    )


@pytest.mark.parametrize("text, expected", [
    ("", ""),
    ("!!! ??? 123", ""),
    ("a", "1"),
    ("Z", "26"),
    ("az", "1 26"),
    ("a, b!", "1 2"),
    ("привет", ""),
    ("café", "3 1 6"),
])
def test_cases(text, expected):
    assert alphabet_position(text) == expected
