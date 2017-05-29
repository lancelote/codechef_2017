import pytest

from solutions.snake_eating import number_of_snakes

EXAMPLES = (
    ('args', 'expected'),
    [
        ((10, [21, 9, 5, 8, 10]), 3),
        ((15, [21, 9, 5, 8, 10]), 1),
        ((100, [1, 2, 3, 4, 5]), 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert number_of_snakes(*args) == expected
