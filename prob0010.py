"""
Problem 10: Summation of primes.

"""

import argparse
import numpy as np
import pandas as pd
import sys

def main(number, description, verbose = False):
    if number < 2:
        raise ValueError("The parsed number must be an integer greater or equal 2.")

    if description:
        print(__doc__)

    n = number

    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p * p, n, p):
                sieve[i] = False
    return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('-d','--description', action='store_true', default=False)
    args = parser.parse_args()
    sol = main(**vars(args))
    print(f'Solution: {sol}')
