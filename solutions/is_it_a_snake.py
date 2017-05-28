class Position:
    def __init__(self, x, y, grid):
        self.x = self.prev_x = x
        self.y = self.prev_y = y
        self.grid = grid

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __str__(self):
        return 'Position(%d, %d)' % (self.x, self.y)

    __repr__ = __str__

    def up(self):
        """Check if step up is allowed."""
        if self.y == 0:
            return False  # Already at top
        elif self.grid[self.y - 1][self.x] == '.':
            return False  # No segment above
        elif self.y - 1 == self.prev_y:
            return False  # Already visited
        return True

    def down(self):
        """Check if step down is allowed."""
        if self.y == 1:
            return False  # Already at bottom
        elif self.grid[self.y + 1][self.x] == '.':
            return False  # No segment below
        elif self.y + 1 == self.prev_y:
            return False  # Already visited
        return True

    def right(self):
        """Check if step right is allowed."""
        if self.x == len(self.grid[0]) - 1:
            return False  # Already on the right end
        elif self.grid[self.y][self.x + 1] == '.':
            return False  # No segment right
        return True

    def remember_position(self):
        """Save current coordinates."""
        self.prev_x = self.x
        self.prev_y = self.y

    def step(self):
        """Perform a step UP, DOWN or RIGHT if possible."""
        if self.up():
            self.remember_position()
            self.y -= 1
            return True
        elif self.down():
            self.remember_position()
            self.y += 1
            return True
        elif self.right():
            self.remember_position()
            self.x += 1
            return True
        return False


def start_positions(grid):
    """Get the most left-top # sign coordinates."""
    starts = []
    found = False
    for x in range(len(grid[0])):
        for y in [0, 1]:
            if grid[y][x] == '#':
                starts.append(Position(x, y, grid))
                found = True
        if found:
            return starts
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
    segments = count_segments(grid)
    positions = start_positions(grid)
    for position in positions:
        steps = 1
        while position.step():
            steps += 1
        if segments == steps:
            return True
    return False


def main():
    n = int(input())
    for _ in range(n):
        _ = input()
        first_line = input()
        second_line = input()
        result = is_snake([first_line, second_line])
        print('yes' if result else 'no')


if __name__ == '__main__':
    main()
