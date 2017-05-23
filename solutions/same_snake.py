class Snake:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def coordinates(self):
        """Return tuple of head & tail coordinates."""
        return self.x1, self.y1, self.x2, self.y2

    def __str__(self):
        return 'Snake(%d, %d, %d, %d)' % self.coordinates()

    __repr__ = __str__


def is_the_same(snake1, snake2):
    raise NotImplementedError


if __name__ == '__main__':
    pass
