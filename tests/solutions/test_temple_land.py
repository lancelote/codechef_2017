import pytest

from solutions.temple_land import is_valid_line, main
from tests.helpers import controlled_call

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
        (("1 2 3 4 5 6 7 8 9 10 11 10 9 8 7 6 5 4 3 2 1", 21), True),
        (("11 22 33", 3), False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_valid_line(*arg) == expected


def test_solution_output():
    task = """7
5
1 2 3 2 1
7
2 3 4 5 4 3 2
5
1 2 3 4 3
5
1 3 5 3 1
7
1 2 3 4 3 2 1
4
1 2 3 2
4
1 2 2 1"""
    expected_result = """yes
no
no
no
yes
no
no"""
    assert controlled_call(task, main) == expected_result
