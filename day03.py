import re
import numpy as np
import sys
import pathlib

class SolveDay03:
    def __init__(self, puzzle_input):
        self.data = self.parse1(puzzle_input)
        self.puzzle_input = puzzle_input

    def parse1(self, puzzle_input):
        """Returns clean list of commands"""
        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        return re.findall(pattern, puzzle_input)

    def part1(self):
        """Solves part 1: Loops through multiplication list and sums the products"""
        mult_list = self.data
        total = 0
        for multiplication in mult_list:
            fact1,fact2 = map(int,multiplication[4:-1].split(','))
            total += fact1 * fact2
        return total

    def part2(self):
        """Solves Part2: Splits string, and only add mul(n,n) after looking for 'do/don't' pattern"""
        # Patterns to search for mul(n,n)
        pattern_for_split = r"(mul\(\d{1,3},\d{1,3}\))"
        pattern = r"mul\(\d{1,3},\d{1,3}\)"

        list_commands = re.split(pattern_for_split, self.puzzle_input)
        total = 0
        enabled = True
        for command in list_commands:
            if re.match(pattern, command) and enabled:
                fact1, fact2 = map(int, command[4:-1].split(','))
                total += fact1 * fact2
            if re.search(r"""don't\(\)""", command):
                enabled = False
            if re.search(r"""do\(\)""", command):
                enabled = True
        return total

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f'{path}:')
        puzzle_input = pathlib.Path(path).read_text().strip()
        sol1, sol2 = SolveDay03(puzzle_input).part1(), SolveDay03(puzzle_input).part2()
        print(f'This is part1: {sol1}\nThis is part2: {sol2}')


