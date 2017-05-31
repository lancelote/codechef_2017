def get_winner(voters):
    voter = ''
    snakes = 0
    mongooses = 0
    can_be_eaten = False

    for voter in voters:
        if voter == 'm':
            can_be_eaten = True
            mongooses += 1
        elif voter == 's':
            if can_be_eaten:
                can_be_eaten = False
            else:
                snakes += 1

    # Last mongooses can eat previous snake
    if voter == 'm' and snakes:
        snakes -= 1

    if snakes > mongooses:
        return 'snakes'
    elif mongooses > snakes:
        return 'mongooses'
    else:
        return 'tie'


def main():
    n = int(input())
    for _ in range(n):
        print(get_winner(input()))


if __name__ == '__main__':
    main()
