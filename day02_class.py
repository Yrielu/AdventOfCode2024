
import pathlib
import sys
import numpy as np

class SolveDay02:
    def __init__(self, puzzle_input):
        self.data = self.parse(puzzle_input)
        self.solutions = self.solve()


    def parse(self, puzzle_input):
        """Parse input into a list of lists."""
        data = [[int(str_num) for str_num in line.split(' ')] for line in puzzle_input.split('\n')]
        return data


    def isSafe(self, line):
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

    def part1(self):
        """Solve part 1: Count the number of safe reports."""
        return len([report for report in self.data if self.isSafe(report)])

    def problemDampener(self, line):
        """Check if removing one element makes the line safe."""
        if self.isSafe(line):
            return True
        else:
            count = 0
            while count < len(line):
                new_line = line[:count] + line[count + 1:]
                if self.isSafe(new_line):
                    return True
                count += 1

            return False

    def part2(self):
        """Solve part 2."""
        return len([report for report in self.data if self.problemDampener(report)])

    def solve(self):
        """Solve the puzzle for the given input."""
        return self.part1(), self.part2()

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = SolveDay02(puzzle_input).solve()
        print("\n".join(str(solution) for solution in solutions))