import pytest

from solutions.is_it_a_snake import Position, start_position, count_segments


@pytest.mark.parametrize('grid,start', [
    (['.#.', '#.#'], (0, 1)),
    (['#.#', '.#.'], (0, 0)),
    (['..#', '..#'], (2, 0)),
    (['#..', '#..'], (0, 0)),
    (['...', '..#'], (2, 1)),
    (['..', '##'], (0, 1)),
])
def test_start_position(grid, start):
    assert start_position(grid) == Position(*start, grid=grid)


@pytest.mark.parametrize('grid,total', [
    (['...', '..#'], 1),
    (['###', '###'], 6),
    (['.#.', '.#.'], 2),
    (['.', '#'], 1),
])
def test_count_segments(grid, total):
    assert count_segments(grid) == total


@pytest.mark.parametrize('position,expected', [
    (Position(2, 1, ['#', '.']), (2, 1)),
    (Position(1, 2, ['#', '.']), (1, 2)),
])
def test_position_init(position, expected):
    assert (position.x, position.y) == expected
    assert (position.prev_x, position.prev_y) == expected
    assert position.grid == ['#', '.']


def test_position_up_already_top():
    position = Position(0, 0, ['#', '.'])
    assert position.up() is False


def test_position_up_no_segment_above():
    position = Position(0, 1, ['.', '#'])
    assert position.up() is False


def test_position_up_already_visited():
    position = Position(0, 1, ['#', '#'])
    position.prev_x, position.prev_y = 0, 0
    assert position.up() is False


def test_position_up_ok():
    position = Position(0, 1, ['#', '#'])
    assert position.up() is True


def test_position_down_already_bottom():
    position = Position(0, 1, ['.', '#'])
    assert position.down() is False


def test_position_down_no_segment_below():
    position = Position(0, 0, ['#', '.'])
    assert position.down() is False


def test_position_down_already_visited():
    position = Position(0, 0, ['#', '#'])
    position.prev_x, position.prev_y = 0, 1
    assert position.down() is False


def test_position_down_ok():
    position = Position(0, 0, ['#', '#'])
    assert position.down() is True


def test_position_right_already_end():
    position = Position(0, 0, ['#', '#'])
    assert position.right() is False


def test_position_right_no_segment_right():
    position = Position(0, 0, ['#.', '##'])
    assert position.right() is False


def test_position_right_ok():
    position = Position(0, 0, ['##', '..'])
    assert position.right() is True


def test_position_step_1():
    position = Position(0, 0, ['##', '##'])
    position.step()
    assert (position.x, position.y) == (0, 1)
    position.step()
    assert (position.x, position.y) == (1, 1)
    position.step()
    assert (position.x, position.y) == (1, 0)
