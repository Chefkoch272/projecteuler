"""
Problem 7

10001st prime

"""

import argparse
import help_functions

def main(number, description):
    if description:
        print(__doc__)
    n=2
    primes=[2]
    length = len(primes)
    while length < number:
        prime=True
        for p in primes:
            if help_functions.is_divisible(n,p):
                prime=False
                break
        if prime:
            primes.append(n)
        n=n+1
        length=len(primes)
    return primes

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int)
    # parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('-d','--description', action='store_true', default=False)
    args = parser.parse_args()
    sol = main(**vars(args))
    print(f'Solution: {sol[-1]}')