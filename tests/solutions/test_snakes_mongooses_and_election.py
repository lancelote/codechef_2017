import pytest

from solutions.snakes_mongooses_and_election import election

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('sm', 'mongooses'),
        ('ssm', 'tie'),
        ('sms', 'tie'),
        ('ssmmmssss', 'snakes'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert election(arg) == expected