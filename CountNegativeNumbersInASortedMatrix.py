def count_negatives(grid):
    m = len(grid)
    n = len(grid[0])

    row = m - 1
    col = 0
    count = 0

    while row >= 0 and col < n:
        if grid[row][col] < 0:

            count += n - col
            row -= 1
        else:
            col += 1

    return count


grid = [[5, 3, 2, -1], [3, 2, 1, -2], [2, 1, 0, -3], [1, 0, -1, -4]]
print(count_negatives(grid))
