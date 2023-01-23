###############################################################################
# Day 10, Task 1                                                              #
###############################################################################

import aoc_util

day = 10
data_str = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


checkpoints = [20, 60, 100, 140, 180, 220]


def task(data_set: list[str]) -> int:
    cycle = 0
    register = 1
    ret = 0

    pixels = []

    for l in data_set:
        increase = 0

        if not l.startswith("noop"):
            if register - 1 <= (cycle - 1) % 40 + 1 <= register + 1:
                pixels.append("█")
            else:
                pixels.append(" ")

            cycle += 1
            if cycle in checkpoints:
                ret += cycle * register

            num = l.split()[1]
            number = int(num)
            increase = number
        
        if register - 1 <= cycle % 40 <= register + 1:
                pixels.append("█")
        else:
            pixels.append(" ")
        cycle += 1
        
        if cycle in checkpoints:
            ret += cycle * register

        register += increase

        if cycle >= 240:
            break


    for i in range(6):
        print("".join(pixels[40 * i:40*(i+1)]))

    return 0


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
