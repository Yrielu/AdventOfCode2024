import numpy as np
import pathlib
import sys
import io

def parse(puzzle_input):
    """Parse the puzzle input into NumPy array"""
    try:
        return np.loadtxt(io.StringIO(puzzle_input), dtype=int, unpack=True)
    except ValueError as e:
        raise ValueError(f"Error parsing data: {e}")

def solve_part1(data):
    """Solves part 1"""
    col1 = np.sort(data[0])
    col2 = np.sort(data[1])
    return sum(abs(col1-col2))

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text()

        data = parse(puzzle_input)
        print(solve_part1(data))




