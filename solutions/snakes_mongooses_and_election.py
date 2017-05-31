def election(line):
    line = line.replace('sm', 'M')
    line = line.replace('ms', 'M')
    line = line.lower()
    snakes = line.count('s')
    mongooses = line.count('m')
    if snakes > mongooses:
        return "snakes"
    if snakes < mongooses:
        return "mongooses"
    else:
        return "tie"


def main():
    n = int(input())
    for _ in range(n):
        print(election(input()))


if __name__ == '__main__':
    main()