###############################################################################
# Day 3, Task 2                                                               #
###############################################################################

import aoc_util

day = 3
data_str = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def task(data_set: list[str]) -> int:
    prios = 0

    for line in data_set:
        letter = set(line[:len(line)//2]) \
            .intersection(set(line[len(line)//2:])) \
            .pop()

        ord_letter = ord(letter)

        if ord_letter >= ord("a"):
            delta = ord_letter - ord("a") + 1
        else:
            delta = ord_letter - ord("A") + 27

        prios += delta

    return prios
            


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
