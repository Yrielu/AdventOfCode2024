
import pathlib
import sys
import numpy as np

def parse(puzzle_input):
    """Parse input."""
    data = [[int(str_num) for str_num in line.split(' ')] for line in puzzle_input.split('\n')]

    return data

def part1(data):
    """Solve part 1."""
    n_unsafe = 0
    #Loop through report/lines
    for line in data:
        prev_num = line[0]
        diff_list = []
        #Loop through levels/num
        for num in line:
            diff_list += [prev_num - num]
            prev_num = num

        all_incr_decr = all(i == np.sign(diff_list[1:])[0] for i in np.sign(diff_list[1:]))
        # Check for steps bigger than 3
        if any([abs(diff) > 3 for diff in diff_list]):
            n_unsafe += 1
        #Check that levels are either all increasing or all decreasing
        elif not all_incr_decr:
            n_unsafe += 1

    return len(data) - n_unsafe


def part2(data):
    """Solve part 2."""
    pass

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