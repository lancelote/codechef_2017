import pytest

from solutions.temp_a_temple_of_snakes import number_of_operations

EXAMPLES = (
    ('args', 'expected'),
    [
        ((3, '1 2 1'), 0),
        ((5, '1 2 6 2 1'), 3),
        ((5, '1 2 9 2 1'), 6),
        ((7, '1 2 3 4 3 2 1'), 0),
        ((7, '1 6 3 4 3 2 1'), 4),
        ((5, '1 2 2 2 1'), 4),
        # ((7, '0 0 3 4 3 2 1'), 4),
        # ((5, '0 1 2 1 1'), 1),
        # ((5, '1 2 1 1 0'), 1),
        # ((4, '1 1 2 1'), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert number_of_operations(*args) == expected


# 0 1 2 3 2 1 0
