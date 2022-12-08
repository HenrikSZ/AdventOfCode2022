###############################################################################
# Day 7, Task 1                                                               #
###############################################################################

from collections import defaultdict
import aoc_util

day = 7
data_str = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def task(data_set: list[str]) -> int:
    file_to_size = defaultdict(lambda: 0)

    paths = []

    for line in data_set:
        if line.startswith("$"):
            command = line.split(" ")
            
            if command[1] == "cd":
                if command[2] == "..":
                    paths.pop()
                else:
                    if len(paths) == 0:
                        paths.append(command[2])
                    else:
                        paths.append(paths[-1] + command[2] + "/")
            
        else:
            args = line.split(" ")
            if args[0].isdigit():
                for p in paths:
                    file_to_size[p] += int(args[0])

    return sum(x for x in file_to_size.values() if x <= 100_000)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
