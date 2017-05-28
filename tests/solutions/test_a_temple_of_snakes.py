import pytest

from solutions.a_temple_of_snakes import number_of_operations, create_list_of_lines

EXAMPLES = (
    ('args', 'expected'),
    [
        ((3, '1 2 1'), 0),
        ((5, '1 2 6 2 1'), 3),
        ((5, '1 2 9 2 1'), 6),
        ((7, '1 2 3 4 3 2 1'), 0),
        ((7, '1 6 3 4 3 2 1'), 4),
        ((5, '1 2 2 2 1'), 4),
        ((7, '0 0 3 4 3 2 1'), 4),
        ((5, '0 1 2 1 1'), 1),
        ((5, '1 2 1 1 0'), 1),
        ((4, '1 1 2 1'), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert number_of_operations(*args) == expected


@pytest.mark.parametrize('line,new_length,expected', [
    ([1, 2, 3, 4, 5], 3, [[1, 2, 3], [2, 3, 4], [3, 4, 5]]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]]),
    ([1, 2, 3, 4, 5, 6, 7], 5, [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]),
    ([1, 2, 3, 4], 3, [[1, 2, 3], [2, 3, 4]]),
])
def test_create_list_of_lines(line, new_length, expected):
    assert create_list_of_lines(line, new_length) == expected
