def get_max_diff_between_neighbours(list_, rows, cols, i, j):
    rmin = i - 1 if i - 1 >= 0 else 0
    rmax = i + 1 if i + 1 < rows else i
    cmin = j - 1 if j - 1 >= 0 else 0
    cmax = j + 1 if j + 1 < cols else j

    diff_between_neighbours = []

    for x in range(rmin, rmax + 1):
        for y in range(cmin, cmax + 1):
            diff_between_neighbours.append(list_[x][y] - list_[i][j])

    return max(diff_between_neighbours)


def get_difference(list_, rows, cols):
    difference = []
    
    for i in range(rows):
        for j in range(cols):
            difference.append(get_max_diff_between_neighbours(list_, rows, cols, i, j))

    return max(difference)


def create_new_list(list_, rows, cols):

    new_list = [[] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            rmin = i - 1 if i - 1 >= 0 else 0
            rmax = i + 1 if i + 1 < rows else i
            cmin = j - 1 if j - 1 >= 0 else 0
            cmax = j + 1 if j + 1 < cols else j
            neighbours_wealth = []

            for x in range(rmin, rmax + 1):
                for y in range(cmin, cmax + 1):
                    neighbours_wealth.append(list_[x][y])
            highest_wealth = max(neighbours_wealth)
            
            new_list[i].append(highest_wealth)

    return new_list

def get_number_of_hours(list_, rows, cols):
    list_ = [list(map(int, line.split())) for line in list_]
    hours = 0
    difference = get_difference(list_, rows, cols)
    while difference > 0:
        hours += 1
        list_ = create_new_list(list_, rows, cols)
        difference = get_difference(list_, rows, cols)
    return hours


def main():
    number_of_tests = int(input())
    for _ in range(number_of_tests):
        n, m = map(int, input().split())
        list_ = []
        for __ in range(n):
            list_.append(input())
        print(get_number_of_hours(list_, n, m))


if __name__ == '__main__':
    main()