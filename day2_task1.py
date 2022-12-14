###############################################################################
# Day 2, Task 1                                                               #
###############################################################################

import aoc_util

day = 2
data_str = """A Y
B X
C Z"""


def task(data_set: list[str]) -> int:
    s = 0

    for l in data_set:
        opponent, me = l.split()
        if me == "X":
            s += 1
            if opponent == "A":
                s += 3
            elif opponent == "C":
                s += 6
        elif me == "Y":
            s += 2
            if opponent == "B":
                s += 3
            elif opponent == "A":
                s += 6
        elif me == "Z":
            s += 3
            if opponent == "C":
                s += 3
            elif opponent == "B":
                s += 6

    return s


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
