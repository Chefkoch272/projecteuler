"""
Problem 5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

import argparse
import pandas as pd

def main():
    return 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--description', action='store_true',
                        default=False)
    args = parser.parse_args()
    if args.description:
        print(__doc__)
    sol = main()
    print(f'Solution: {sol}')