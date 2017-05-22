import pytest

from solutions.temple_land import is_valid_line

EXAMPLES = (
    ('arg', 'expected'),
    [
        (("1 2 3 2 1", 5), True),
        (("2 3 4 5 4 3 2", 7), False),
        (("1 2 3 4 3", 5), False),
        (("1 3 5 3 1", 5), False),
        (("1 2 3 4 3 2 1", 7), True),
        (("1 2 3 2", 4), False),
        (("1 2 2 1", 4), False),
        (("0 1 0", 3), False),
        (("1 2 3 4 5 6 7 6 5 4 3 2 1", 13), True),
        (("1 2 3 2 1 0 1", 6), False),
        (("1 2 1", 3), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_valid_line(*arg) == expected
