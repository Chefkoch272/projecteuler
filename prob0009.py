"""
Problem 9

Special Pythagorean triplet

"""

import argparse

def main(number, description, verbose = False):
    if description:
        print(__doc__)

    solution = []

    for c in range(number+1):
        c_diff = number - c
        for b in range(c_diff+1):
            a = c_diff - b
            if a < b and b < c:
                if verbose:
                    print(c, b, a)
                if a**2 + b**2 == c**2:
                    solution.append(a * b * c)

    return solution

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('-d','--description', action='store_true', default=False)
    args = parser.parse_args()
    sol = main(**vars(args))
    print(f'Solution: {sol}')
