###############################################################################
# Day 1, Task 2                                                               #
###############################################################################

import aoc_util

day = 1
data_str = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def task(data_set: list[str]) -> int:
    counter = 0
    max_list = []

    for s in data_set:
        if s == "":
            max_list += [counter]
            counter = 0
        else:
            counter += int(s)

    max_list += [counter]

    return sum(sorted(max_list)[-3:])


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
