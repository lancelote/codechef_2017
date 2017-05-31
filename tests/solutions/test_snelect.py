import pytest

from solutions.snelect import get_winner


@pytest.mark.parametrize('voters,winner', [
    ('sm', 'mongooses'),
    ('ssm', 'tie'),
    ('sms', 'tie'),
    ('ssmmmssss', 'snakes'),
])
def test_winner(voters, winner):
    assert get_winner(voters) == winner
