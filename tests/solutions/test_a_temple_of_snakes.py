import pytest

from solutions.a_temple_of_snakes import number_of_operations

EXAMPLES = (
    ('args', 'expected'),
    [
        (('1 2 1', 3), 0),
        # (('1 1 2 1', 4), 1),
        (('1 2 6 2 1', 5), 3),
        (('1 2 2 2 1', 5), None),
        
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert number_of_operations(*args) == expected


# 0 1 2 3 2 1 0
