import pytest

from solutions.snakes_capitalism_to_socialism import get_number_of_hours, get_max_diff_between_neighbours

EXAMPLES = (
    ('list_', 'rows', 'cols', 'expected'),
    [
        (['1 1',
          '1 1'], 2, 2, 0),
        (['1 1',
          '1 2'], 2, 2, 1),
        (['1 2 1 2',
          '1 1 1 2',
          '1 1 2 2'], 3, 4, 2),
    ]
)

@pytest.mark.parametrize(*EXAMPLES)
def test_get_number_of_hours(list_, rows, cols, expected):
    assert get_number_of_hours(list_, rows, cols) == expected
    

@pytest.mark.parametrize('args,expected', [
        (([[1, 2, 1, 2], [1, 1, 1, 2], [1, 1, 2, 2]], 3, 4, 1, 1), 1),
        (([[1, 2, 1, 2], [1, 1, 5, 2], [1, 1, 2, 2]], 3, 4, 1, 1), 4),
        (([[1, 2, 1, 2],
          [1, 1, 5, 2],
          [1, 1, 2, 2],
          [1, 1, 2, 2]], 4, 4, 2, 2), 3),
        (([[1, 2, 5, 2],
          [1, 1, 1, 2],
          [1, 1, 2, 2],
          [1, 1, 2, 2]], 4, 4, 1, 1), 4),
    ])
def test_get_max_diff_between_neighbours(args, expected):
    assert get_max_diff_between_neighbours(*args) == expected
