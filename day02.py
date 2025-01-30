
import pathlib
import sys
from itertools import count
import numpy as np

def parse(puzzle_input):
    """Parse input."""
    data = [[int(str_num) for str_num in line.split(' ')] for line in puzzle_input.split('\n')]

    return data

def part1(data):
    """Solve part 1: Count the number of safe reports."""
    def isSafe(line):
        """Does checks in line and return True if passed all checks"""
        # Loop through levels/num
        prev_num = line[0]
        diff_list = []
        for num in line:
            diff_list += [prev_num - num]
            prev_num = num

        all_incr_decre = all(i == np.sign(diff_list[1:])[0] for i in np.sign(diff_list[1:]))
        # Check for steps bigger than 3
        if any([abs(diff) > 3 for diff in diff_list]):
            return False
        # Check that levels are either all increasing or all decreasing
        elif not all_incr_decre:
            return False
        return True

    return len([report for report in data if isSafe(report)])


def part2(data):
    """Solve part 2."""
    def isSafe(line):
        """Does checks in line and return True if passed all checks"""
        # Loop through levels/num
        prev_num = line[0]
        diff_list = []
        for num in line:
            diff_list += [prev_num - num]
            prev_num = num

        all_incr_decre = all(i == np.sign(diff_list[1:])[0] for i in np.sign(diff_list[1:]))
        # Check for steps bigger than 3
        if any([abs(diff) > 3 for diff in diff_list]):
            return False
        # Check that levels are either all increasing or all decreasing
        elif not all_incr_decre:
            return False
        return True

    def problemDampener(line):
        if isSafe(line):
            return True
        else:
            count = 0
            while count < len(line):
                new_line = line[:count] + line[count + 1:]
                if isSafe(new_line):
                    return True
                count += 1

            return False

    return len([report for report in data if problemDampener(report)])

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))