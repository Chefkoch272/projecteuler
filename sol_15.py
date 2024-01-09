"""
ideas:
- save for each grid size how many paths there are
- each next bigger grid consists of already explored smaller sub-grids (think of minors in linear algebra)


a = 2 * (1)
b = 2 * (1 + a)
c = 2 * (1 + a + b)
d = 2 * (1 + a + b + c)

n0 = 0
n1 = 2 * (1 + n0)
n2 = 2 * (1 + n0 + n1)
n3 = 2 * (1 + n0 + n1 + n2)

based on binomial coefficent (n _over_ k)
"""

import math

def binomial_coeff(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

gridsize = 20
print(binomial_coeff(2*gridsize,gridsize))