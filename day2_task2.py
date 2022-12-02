###############################################################################
# Day 2, Task 2                                                               #
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
            if opponent == "A":
                s += 3
            elif opponent == "B":
                s += 1
            elif opponent == "C":
                s += 2
        elif me == "Y":
            s += 3
            if opponent == "A":
                s += 1
            elif opponent == "B":
                s += 2
            elif opponent == "C":
                s += 3
        elif me == "Z":
            s += 6
            if opponent == "A":
                s += 2
            elif opponent == "B":
                s += 3
            elif opponent == "C":
                s += 1

    return s


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
