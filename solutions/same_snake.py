class Snake:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
    
    @property
    def head(self):
        return self.x1, self.y1
    
    @property
    def tail(self):
        return self.x2, self.y2
    
    def common_end(self, other):
        return self.head in (other.head, other.tail) or \
               self.tail in (other.head, other.tail)

    def coordinates(self):
        """Return tuple of head & tail coordinates."""
        return self.x1, self.y1, self.x2, self.y2
    
    def on_same_horizontal(self, other):
        return self.y1 == self.y2 == other.y1 == other.y2

    def on_same_vertical(self, other):
        return self.x1 == self.x2 == other.x1 == other.x2

    def __str__(self):
        return 'Snake(%d, %d, %d, %d)' % self.coordinates()

    __repr__ = __str__


def is_the_same(snake1, snake2):
    if snake1.on_same_horizontal(snake2):
        return all([
            min(snake1.x1, snake1.x2) < min(snake2.x1, snake2.x2),
            min(snake2.x1, snake2.x2) < max(snake1.x1, snake1.x2),
            max(snake1.x1, snake1.x2) < max(snake2.x1, snake2.x2)
        ]) or \
               all([
            min(snake2.x1, snake2.x2) < min(snake1.x1, snake1.x2),
            min(snake1.x1, snake1.x2) < max(snake2.x1, snake2.x2),
            max(snake2.x1, snake2.x2) < max(snake1.x1, snake1.x2)
        ])
    elif snake1.on_same_vertical(snake2):
        return all([
            min(snake1.y1, snake1.y2) < min(snake2.y1, snake2.y2),
            min(snake2.y1, snake2.y2) < max(snake1.y1, snake1.y2),
            max(snake1.y1, snake1.y2) < max(snake2.y1, snake2.y2)
        ]) or \
               all([
            min(snake2.y1, snake2.y2) < min(snake1.y1, snake1.y2),
            min(snake1.y1, snake1.y2) < max(snake2.y1, snake2.y2),
            max(snake2.y1, snake2.y2) < max(snake1.y1, snake1.y2)
        ])
    else:
        return snake1.common_end(snake2)

  

def main():
    n = int(input())
    while n > 0:
        snake1 = Snake(*input().split())
        snake2 = Snake(*input().split())
        if is_the_same(snake1, snake2):
            print("yes")
        else:
            print("no")
        n -= 1


if __name__ == '__main__':
    main()
