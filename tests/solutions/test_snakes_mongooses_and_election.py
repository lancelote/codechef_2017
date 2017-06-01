import pytest

from solutions.snakes_mongooses_and_election import election


@pytest.mark.parametrize('voters,winner', [
    ('sm', 'mongooses'),
    ('ssm', 'tie'),
    ('sms', 'tie'),
    ('ssmmmssss', 'snakes'),
    ('s', 'snakes'),
    ('m', 'mongooses'),
    ('sms', 'tie'),
    ('sssmsm', 'tie'),
    ('sssmm', 'tie'),
    ('ssssmm', 'snakes'),
    ('', 'tie'),
    ('ssm', 'tie'),
    ('mssm', 'mongooses'),
    ('msssm', 'mongooses'),
    ('mssssm', 'tie'),
    ('mm', 'mongooses'),
    ('smmss', 'mongooses'),
])
def test_winner(voters, winner):
    assert election(voters) == winner
