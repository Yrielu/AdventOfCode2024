import re
import numpy as np
import sys
import pathlib

test = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

class SolveDay03:
    def __init__(self, puzzle_input):
        self.data = self.parse(puzzle_input)

    def parse(self, puzzle_input):
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

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f'{path}:')
        puzzle_input = pathlib.Path(path).read_text().strip()
        solution = SolveDay03(puzzle_input).part1()
        print(f'{solution}')


