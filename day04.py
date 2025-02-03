import re
import sys
import pathlib
from operator import invert

class SolveDay04:
    def __init__(self, puzzle_input):
        self.hor_list = self.parse(puzzle_input)

    def parse(self, puzzle_input):
        """Converts puzzle input into a list of strings, line by line"""
        return puzzle_input.split('\n')

    def make_vertical(self):
        """Make horizontal list of string into their vertical orientation"""
        ver_list = []
        line_length = len(self.hor_list[0])
        count = 0
        while count < line_length:
            ver_line = ''
            for line in self.hor_list:
                ver_line += line[count]
            ver_list += [ver_line]
            count += 1
        return ver_list

    def make_diagonal(self):
        """Makes horizontal list of string into a list of their diagonal, first from left to right
        orientation and then from right to left by using the inverse"""
        diag_list = []

        inverse_diag = [line[::-1] for line in self.hor_list]
        diag_orientation = [self.hor_list, inverse_diag]
        for diagonal in diag_orientation:
            # Upper left to right diagonals
            count = 0
            line_length = len(diagonal[0])
            while count < line_length:
                diag_line = ''
                diag_count = 0
                for line in diagonal:
                    if diag_count + count + 1 > len(line):
                        break
                    diag_line += line[diag_count + count]
                    diag_count += 1
                diag_list += [diag_line]
                count += 1

            # Lower left to right diagonals
            count = 0
            while count < len(diagonal) - 1:
                diag_line = ''
                diag_count = 0
                for line in diagonal[count + 1:]:
                    diag_line += line[diag_count]
                    diag_count += 1
                diag_list += [diag_line]
                count += 1

        return diag_list

    def count_XMAS(self, list_lines):
        match_list = []
        for item in list_lines:
            match_list += re.findall('XMAS', item)
            match_list += re.findall('XMAS'[::-1], item)
        return len(match_list)

    def part1(self):
        total = self.count_XMAS(self.hor_list) + self.count_XMAS(self.make_vertical()) + self.count_XMAS(self.make_diagonal())
        return total

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f'{path}:')
        puzzle_input = pathlib.Path(path).read_text().strip()
        sol1 = SolveDay04(puzzle_input).part1()
        print(f'This is part1: {sol1}\n')
