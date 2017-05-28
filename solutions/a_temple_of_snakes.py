import math
from itertools import chain


def create_ideal_ground(length):
    middle = math.ceil(length / 2)
    return list(chain(range(1, middle + 1), range(middle - 1, 0, -1)))


def higher_than_ideal(line, ideal_ground):
    for block, ideal_block in zip(line, ideal_ground):
        if block < ideal_block:
            return False
    return True


def number_of_operations(length, line):
    line = list(map(int, line.split()))
    sum_line = sum(line)
    max_ideal_length = int(math.sqrt(sum_line)) * 2 - 1

    for ideal_length in range(length, 0, -1):
        ideal_ground = create_ideal_ground(ideal_length)
        sum_ideal = sum(ideal_ground)
        length_diff = length - ideal_length
        for i in range(length_diff):
            if higher_than_ideal(line[i:-length_diff+i], ideal_ground):
                return sum_line - sum_ideal
        last = line[-ideal_length:]
        if higher_than_ideal(last, ideal_ground):
            return sum_line - sum_ideal


def main():
    n = int(input())
    while n > 0:
        length = int(input())
        line = input()
        print(number_of_operations(length, line))
        n -= 1


if __name__ == '__main__':
    main()
