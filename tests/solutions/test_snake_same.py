import pytest

from solutions.same_snake import is_the_same, Snake

EXAMPLES = (
    ('args', 'expected'),
    [
        ((Snake(2, 1, 8, 1), Snake(11, 1, 7, 1)), True),
        ((Snake(2, 1, 8, 1), Snake(11, 1, 9, 1)), True),
        ((Snake(2, 1, 8, 1), Snake(3, 1, 3, -2)), True),
        ((Snake(2, 1, 8, 1), Snake(2, 1, 2, -2)), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert is_the_same(*args) == expected


def test_snake_coordinates():
    assert Snake(1, 2, 3, 4).coordinates() == (1, 2, 3, 4)


def test_snake_str():
    assert str(Snake(1, 2, 3, 4)) == 'Snake(1, 2, 3, 4)'
