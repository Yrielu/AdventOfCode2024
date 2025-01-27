import numpy as np

#data = np.loadtxt('day01.txt', dtype=int, unpack = True)
data = np.array([[3,4,2,1,3,3],[4,3,5,3,9,3]])


def solve_part2(data):
    """Solves part 2"""
    left_col = np.unique_counts(data[0])
    right_col = np.unique_counts(data[1])
    left_tot = np.unique_counts(data[0])[0] * np.unique_counts(data[0])[1]

    count = 0
    for value in left_col[0]:
        if value in right_col[0]:
            left_tot[count] *= right_col[1][list(right_col[0]).index(value)]
        else:
            left_tot[count] *= 0
        count += 1

    return np.sum(left_tot)

print(solve_part2(data))