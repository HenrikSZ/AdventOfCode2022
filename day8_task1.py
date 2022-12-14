###############################################################################
# Day 8, Task 1                                                               #
###############################################################################

import aoc_util

day = 8
data_str = """30373
25512
65332
33549
35390"""


def is_visible(grid, row, col):
    height = grid[row][col]

    blocked_sides = 0

    for x in range(0, col):
        if grid[row][x] >= height:
            blocked_sides += 1
            break
    
    for x in range(col + 1, len(grid[row])):
        if grid[row][x] >= height:
            blocked_sides += 1
            break

    for y in range(0, row):
        if grid[y][col] >= height:
            blocked_sides += 1
            break

    for y in range(row + 1, len(grid)):
        if grid[y][col] >= height:
            blocked_sides += 1
            break

    return blocked_sides < 4


def task(data_set: list[str]) -> int:
    count = 0
    grid = []

    for l in data_set:
        grid.append([int(x) for x in l])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_visible(grid, row, col):
                count += 1

    return count


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
