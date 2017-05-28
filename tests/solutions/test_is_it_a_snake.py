import pytest

from solutions.is_it_a_snake import Position, start_position, count_segments


@pytest.mark.parametrize('grid,start', [
    (['.#.', '#.#'], Position(0, 1)),
    (['#.#', '.#.'], Position(0, 0)),
    (['..#', '..#'], Position(2, 0)),
    (['#..', '#..'], Position(0, 0)),
    (['...', '..#'], Position(2, 1)),
])
def test_start_position(grid, start):
    assert start_position(grid) == start


@pytest.mark.parametrize('grid,total', [
    (['...', '..#'], 1),
    (['###', '###'], 6),
    (['.#.', '.#.'], 2),
    (['.', '#'], 1),
])
def test_count_segments(grid, total):
    assert count_segments(grid) == total


@pytest.mark.parametrize('position,expected', [
    (Position(2, 1), (2, 1)),
    (Position(1, 2), (1, 2)),
])
def test_position_init(position, expected):
    assert (position.x, position.y) == expected
