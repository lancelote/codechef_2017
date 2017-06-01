import pytest

from solutions.snakes_capitalism_to_socialism import get_number_of_hours

EXAMPLES = (
    ('grid', 'rows', 'cols', 'expected'),
    [
        (['2 1 1'], 1, 3, 2),
        (['1 1',
          '1 1'], 2, 2, 0),
        (['1 1',
          '1 2'], 2, 2, 1),
        (['1 2 1 2',
          '1 1 1 2',
          '1 1 2 2'], 3, 4, 2),
        (['2 2',
          '1 1',
          '3 3'], 3, 2, 2),
        (['1 1',
          '2 1'], 2, 2, 1),
        (['1 1 1',
          '1 1 1',
          '2 1 1'], 3, 3, 2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_get_number_of_hours(grid, rows, cols, expected):
    assert get_number_of_hours(grid, rows, cols) == expected
