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


def task(data_set: list[str]) -> int:
    tail_x, tail_y = 0, 0
    start_x, start_y = 0, 0

    positions = set()
    positions.add((tail_x, tail_y))

    for l in data_set:
        direction, steps = l.split()
        
        for _ in range(int(steps)):
            match direction:
                case "U":
                    start_y += 1
                case "D":
                    start_y -= 1
                case "R":
                    start_x += 1
                case "L":
                    start_x -= 1

            if abs(tail_y - start_y) > 1:
                if tail_x != start_x:
                    tail_x += start_x - tail_x
                tail_y += 1 if start_y > tail_y else -1
            elif abs(tail_x - start_x) > 1:
                if tail_y != start_y:
                    tail_y += start_y - tail_y
                tail_x += 1 if start_x > tail_x else -1
            
            positions.add((tail_x, tail_y))
            #print(tail_x, tail_y)

    return len(positions)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
