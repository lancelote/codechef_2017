import math
from itertools import chain


def is_valid_line(line, length):
    line = line.split(' ')
    length = int(length)
    if not length % 2:
        return False
    middle = math.ceil(length / 2)
    for i, digit in enumerate(chain(range(1, middle + 1), range(middle - 1, 0, -1))):
        if digit != int(line[i]):
            return False
    return True


def main():
    n = int(input())
    while n > 0:
        length = input()
        if is_valid_line(input(), length):
            print("yes")
        else:
            print("no")
        n -= 1


if __name__ == '__main__':
    main()
