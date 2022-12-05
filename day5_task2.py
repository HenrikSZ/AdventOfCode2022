###############################################################################
# Day 5, Task 2                                                               #
###############################################################################

import aoc_util

day = 5
data_str = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def parse_line(line: str, l: list[list[str]] = []):
    for index, c in enumerate(line[1:-1:4]):
        if c.isdigit():
            return
        elif not c.isspace():
            while len(l) <= index:
                l.append([])

            l[index].append(c)

    
def perform_restack(line: str, l: list[list[str]] = []):
    instructions = line.split(" ")

    count = int(instructions[1])
    from_stack = int(instructions[3])
    to_stack = int(instructions[5])

    stack = l[from_stack - 1][-count:]
    l[from_stack - 1] = l[from_stack - 1][:-count]
    l[to_stack - 1].extend(stack)


def task(data_set: list[str]) -> int:
    l: list[list[str]] = []
    parsed_stacks = False

    for line in data_set:
        if not parsed_stacks:
            if line == "":
                for stack in l:
                    stack.reverse()
                parsed_stacks = True
            else:
                parse_line(line, l)
        else:
            perform_restack(line, l)

    
    acc = "".join(x[-1] for x in l)
    
    return acc
            


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
