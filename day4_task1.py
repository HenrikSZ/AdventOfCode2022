###############################################################################
# Day 4, Task 1                                                               #
###############################################################################

import aoc_util

day = 4
data_str = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def is_fully_contained(a, b, x, y):
    return x <= a and b <= y


def task(data_set: list[str]) -> int:
    acc = 0

    for p in data_set:
        first, second = p.split(",")
        a, b = [int(x) for x in first.split("-")]
        x, y = [int(x) for x in second.split("-")]

        if is_fully_contained(a, b, x, y) or is_fully_contained(x, y, a, b):
            acc += 1


    return acc
            


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
