import pytest

from solutions.snake_procession import is_valid_line

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("..H..T...HTH....T.", True),
        ("...", True),
        ("H..H..T..T", False),
        ("HT", True),
        (".T...H..H.T", False),
        ("H..T..H", False),
        ("HHT", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_valid_line(arg) == expected
