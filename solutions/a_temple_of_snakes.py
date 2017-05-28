import math
from itertools import chain


def higher_than_ideal(length, line, ideal_ground):
    return all(block >= ideal_block for block, ideal_block in zip(line, ideal_ground))

def ideal_ground_length(length):
    if length % 2:
        return length - 1
    else:
        return length - 2

def number_of_operations(length, line):
    middle = math.ceil(length / 2)
    ideal_ground = list(chain(range(1, middle + 1), range(middle - 1, 0, -1)))
    line = list(map(int, line.split(' ')))
    if length % 2:
        if higher_than_ideal(length, line, ideal_ground):
            return sum(line) - sum(ideal_ground)
        else:
            length -= 2
            middle
            ideal_ground
            for l in line:
                l1 = line[0:-2]
                l2 = line[1:-1]
                l3 = line[2:]
                higher_than_ideal(l, length, ideal_ground)
    else:
        pass

def main():
    n = int(input())
    while n > 0:
        length = input()
        line = input()
        number_of_operations(length, line)
        n -= 1


if __name__ == '__main__':
    main()


# 3


# 3
# 1 2 1

# 4
# 1 1 2 1

# 5
# 0 2 6 2 1
# 1 2 3 2 1


# 1 2 2 4 3 2 1
# 1 2 3 2 1

# 1 2 2 4 3 - -
# - 2 2 4 3 2 -
# - - 2 4 3 2 1

# 0 1 2 3 3 2 1


# max 3

# 0

# 1

# 3