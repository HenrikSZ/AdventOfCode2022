###############################################################################
# Day 8, Task 2                                                               #
###############################################################################

import aoc_util
import functools
import operator

day = 8
data_str = """30373
25512
65332
33549
35390"""


def scenic_score(grid, row, col):
    height = grid[row][col]

    scenic_scores = [0] * 4

    for x in range(col - 1, -1, -1):
        scenic_scores[0] += 1
        if grid[row][x] >= height:
            break
    
    for x in range(col + 1, len(grid[row])):
        scenic_scores[1] += 1
        if grid[row][x] >= height:
            break

    for y in range(row - 1, -1, -1):
        scenic_scores[2] += 1
        if grid[y][col] >= height:
            break

    for y in range(row + 1, len(grid)):
        scenic_scores[3] += 1
        if grid[y][col] >= height:
            break

    return functools.reduce(operator.mul, scenic_scores)


def task(data_set: list[str]) -> int:
    max_score = 0
    grid = []

    for l in data_set:
        grid.append([int(x) for x in l])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            score = scenic_score(grid, row, col)
            max_score = max(score, max_score)

    return max_score


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
