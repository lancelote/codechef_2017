class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def step(self, grid):
        pass


def start_position(grid):
    """Get the most left-top # sign coordinates."""
    for x in range(len(grid[0])):
        for y in [0, 1]:
            if grid[y][x] == '#':
                return Position(x, y)
    raise ValueError('Grid has no # sign')


def count_segments(grid):
    """Count number of # in the grid."""
    total = 0
    for line in grid:
        for item in line:
            if item == '#':
                total += 1
    return total


def is_snake(grid):
    """Check if all segments are visited."""
    steps = 0
    segments = count_segments(grid)
    position = start_position(grid)
    while position.step(grid):
        steps += 1
    return steps == segments


def main():
    n = int(input())
    for _ in range(n):
        first_line = input()
        second_line = input()
        result = is_snake([first_line, second_line])
        print('yes' if result else 'no')


if __name__ == '__main__':
    main()
