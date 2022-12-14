###############################################################################
# Day 1, Task 1                                                               #
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
    max_counter = 0

    for s in data_set:
        if s == "":
            max_counter = max(counter, max_counter)
            counter = 0
        else:
            counter += int(s)

    return max_counter


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
