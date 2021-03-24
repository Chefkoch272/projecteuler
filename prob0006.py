"""
Problem 6

Sum square difference.

________________________________________________________________________________

See https://projecteuler.net/problem=6 .

"""

import argparse
import pandas as pd

def main(n_max, description, verbose):
    if description:
        print(__doc__)
    series = pd.DataFrame(range(1,n_max+1))
    square_of_sum = (series.sum()**2)[0]
    sum_of_squares = ((series * series).sum())[0]
    if verbose:
        print(f'{square_of_sum} - {sum_of_squares} equals following solution.')
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--n_max', type=int, required=True)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('-d','--description', action='store_true', default=False)
    args = parser.parse_args()
    sol = main(**vars(args))
    print(f'Solution: {sol}')