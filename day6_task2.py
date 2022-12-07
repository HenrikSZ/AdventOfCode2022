###############################################################################
# Day 6, Task 1                                                               #
###############################################################################

import aoc_util

day = 6
data_str5 = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
data_str6 = """nppdvjthqldpwncqszvftbrmjlhg"""
data_str7 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
data_str10 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
data_str11 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""


def task(data_set: list[str]) -> int:
    l = data_set[0]

    for i in range(3, len(l)):
        starting_sequence = True

        for j in range(i - 12, i + 1):
            for k in range(i - 13, j):
                if l[j] == l[k]:
                    starting_sequence = False
                    break
            if not starting_sequence:
                break

        if starting_sequence:
            return i + 1

    return 0

            


aoc_util.run_with_data_str(task, data_str5)
aoc_util.run_with_data_str(task, data_str6)
aoc_util.run_with_data_str(task, data_str7)
aoc_util.run_with_data_str(task, data_str10)
aoc_util.run_with_data_str(task, data_str11)
aoc_util.run_with_data_set(task, day)
