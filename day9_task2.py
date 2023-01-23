###############################################################################
# Day 9, Task 1                                                               #
###############################################################################

import aoc_util

day = 9
data_str = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
data_str_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def adjust_knot(knots: list[list[int]], knot: int):
    c, p = knots[knot], knots[knot - 1]

    if abs(c[1] - p[1]) > 1:
        if c[0] != p[0]:
            c[0] += p[0] - c[0]
        if p[1] > c[1]:
            c[1] += 1
        else:
            c[1] -= 1
    elif abs(c[0] - p[0]) > 1:
        if c[1] != p[1]:
            c[1] += p[1] - c[1]
        if p[0] > c[0]:
            c[0] += 1
        else:
            c[0] -= 1


def task(data_set: list[str]) -> int:
    knots = [[0, 0] for _ in range(10)]

    tail_positions = set()
    tail_positions.add((0, 0))

    for l in data_set:
        direction, steps = l.split()
        
        for _ in range(int(steps)):
            match direction:
                case "U":
                    knots[0][1] += 1
                case "D":
                    knots[0][1] -= 1
                case "R":
                    knots[0][0] += 1
                case "L":
                    knots[0][0] -= 1

            for knot in range(1, len(knots)):
                adjust_knot(knots, knot)
            
            tail_positions.add((knots[-1][0], knots[-1][1]))

    return len(tail_positions)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_str(task, data_str_2)
aoc_util.run_with_data_set(task, day)
