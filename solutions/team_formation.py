# 4
  
# total pair
# 2 1

# pairs
# 1 2


# total pair
# 4 1

# pairs
# 1 3


# total pair
# 5 2

# pairs
# 1 2
# 4 5


# total pair
# 5 1

# pairs
# 1 4

def is_valid_team(total):
    return not total % 2


def main():
    n = int(input())
    while n > 0:
        total, pairs = map(int, input().split())
        if is_valid_team(total):
            print("yes")
        else:
            print("no")
        for _ in range(pairs):
            input()
        n -= 1


if __name__ == '__main__':
    main()
