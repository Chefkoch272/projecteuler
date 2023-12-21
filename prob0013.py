import numpy as np

n_first_digits = 10
numbers = np.genfromtxt('prob0013_input')

first_digits = str(sum(numbers)).replace('.','')[:n_first_digits]

print(first_digits)