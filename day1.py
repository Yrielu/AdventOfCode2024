import numpy as np

data = np.loadtxt('day1.txt', dtype = int, unpack=True )
col1 = np.sort(data[0])
col2 = np.sort(data[1])
tot_dist = sum(abs(col1-col2))

print(tot_dist)
