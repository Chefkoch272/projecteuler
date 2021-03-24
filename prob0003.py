"""
Problem 3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import argparse

def main(p):
    # Todo: Repetively divide number n by divisor d until it is not divisible.
    # Todo: Then increase d by 1.

    # Todo: How to check if divisor d is a prime number?
    pass
    return p

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prime_number', type=int)
    # parser.add_argument('-v', '--verbose', action='store_true', default=False)
    args = parser.parse_args()
    sol = main(p=args.prime_number)
    print(f'Solution: {sol}')