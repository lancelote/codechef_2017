def number_of_snakes(limit, snakes):
    """Count number of snakes after eating >= limit."""
    total = 0
    snakes = sorted(snakes)

    while snakes:
        snake = snakes.pop()
        while snake < limit and snakes:
            snakes.pop()
            snake += 1
        if limit - snake > len(snakes):
            break
        total += 1
    return total


def main():
    n = int(input())
    for _ in range(n):
        _, q = input().split()
        q = int(q)
        snakes = list(map(int, input().split()))
        for __ in range(q):
            limit = int(input())
            print(number_of_snakes(limit, snakes))


if __name__ == '__main__':
    main()
