def is_valid_line(line):
    complete_snake = True
    for char in line:
        if char == 'H' and complete_snake:
            complete_snake = False
        elif char == 'T' and not complete_snake:
            complete_snake = True
        elif char == '.':
            continue
        else:
            return False
    return complete_snake


def main():
    n = int(input())
    while n > 0:
        _ = input()
        if is_valid_line(input()):
            print("Valid")
        else:
            print("Invalid")
        n -= 1


if __name__ == '__main__':
    main()
