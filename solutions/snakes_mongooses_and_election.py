def election(voters):
    snakes = 0
    mongooses = 0
    free_snake = False
    free_mongoose = False

    for voter in voters:
        if voter == 's':
            if free_mongoose:
                free_mongoose = False
            else:
                free_snake = True
                snakes += 1
        else:
            if free_snake:
                free_mongoose = False
                free_snake = False
                snakes -= 1
            else:
                free_mongoose = True
            mongooses += 1

    if snakes > mongooses:
        return 'snakes'
    elif mongooses > snakes:
        return 'mongooses'
    else:
        return 'tie'


def main():
    n = int(input())
    for _ in range(n):
        print(election(input()))


if __name__ == '__main__':
    main()
