def create_new_list(grid, rows, cols):
    new_list = [[] for _ in range(rows)]
    changes = False

    for i in range(rows):
        for j in range(cols):
            rmin = i - 1 if i - 1 >= 0 else 0
            rmax = i + 1 if i + 1 < rows else i
            cmin = j - 1 if j - 1 >= 0 else 0
            cmax = j + 1 if j + 1 < cols else j
            neighbours_wealth = []

            for x in range(rmin, rmax + 1):
                for y in range(cmin, cmax + 1):
                    neighbours_wealth.append(grid[x][y])
            highest_wealth = max(neighbours_wealth)

            if grid[i][j] != highest_wealth:
                changes = True
            new_list[i].append(highest_wealth)

    return changes, new_list


def get_number_of_hours(grid, rows, cols):
    grid = [[int(item) for item in line.split()] for line in grid]
    hours = -1
    changes = True
    while changes:
        hours += 1
        changes, grid = create_new_list(grid, rows, cols)
    return hours


def main():
    number_of_tests = int(input())
    for _ in range(number_of_tests):
        n, m = map(int, input().split())
        grid = []
        for __ in range(n):
            grid.append(input())
        print(get_number_of_hours(grid, n, m))


if __name__ == '__main__':
    main()
