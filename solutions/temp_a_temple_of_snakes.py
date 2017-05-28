import math
from itertools import chain


def create_ideal_ground(length):
    middle = math.ceil(length / 2)
    return list(chain(range(1, middle + 1), range(middle - 1, 0, -1)))


def higher_than_ideal(line, ideal_ground):
    return all(block >= ideal_block
               for block, ideal_block in zip(line, ideal_ground))


def create_list_of_lines(line, new_length):
    print(line, new_length)
    new_list_of_lines = []
    length = len(line)
    length_difference = new_length - length
    for i in range(length_difference):
        new_list_of_lines.append(line[i:-length_difference+i])
    new_list_of_lines.append(line[-new_length:])
    return new_list_of_lines


def create_params(length, line):
    if length % 2:
        new_length = length - 1
    else:
        new_length = length - 2
    list_of_lines = create_list_of_lines(line, new_length)
    return new_length, list_of_lines


def number_of_operations(length, line):
    ideal_ground = create_ideal_ground(length)
    line = list(map(int, line.split(' ')))
    if higher_than_ideal(line, ideal_ground):
        return sum(line) - sum(ideal_ground)
    wanted_s = None
    while not wanted_s:
        new_length, list_of_lines = create_params(length, line)
        ideal_ground = create_ideal_ground(new_length)
        if any(higher_than_ideal(new_line, ideal_ground) for new_line in list_of_lines):
            wanted_s = sum(line) - sum(ideal_ground)
            return wanted_s

def main():
    n = int(input())
    while n > 0:
        length = int(input())
        line = input()
        number_of_operations(length, line)
        n -= 1


if __name__ == '__main__':
    main()
