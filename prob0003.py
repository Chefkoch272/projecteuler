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
    prime_factors = []
    n = p
    d = 2
    while n > 1 and n >= d:
        if is_divisible(n,d):
            n = int(n/d)
            prime_factors.append(d)
        else:
            d = d + 1
        # print(f'd: {d} and n: {n}')
    highest_prime_factors = max(prime_factors)
    return highest_prime_factors, prime_factors

def is_divisible(number, divisor):
    return (number % divisor == 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prime_number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('-d','--description', action='store_true', default=False)
    args = parser.parse_args()
    if args.description:
        print(__doc__)
    sol, _ = main(p=args.prime_number)
    print(f'Solution: {sol}')
    if args.verbose:
        print(_)