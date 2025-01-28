import numpy as np

data1 = np.array([[3,4,2,1,3,3],[4,3,5,3,9,3]])



a = [1,-4,1,3]
n_unsafe = 0


if any([abs(num)> 3 for num in a ]):
    print('hi')

elif len(a) < 20:
    print('yes')
#print(all(i == a[0] for i in a))
# a= np.sign([1,2,3,4])
# print(not all(i == a[0] for i in a))