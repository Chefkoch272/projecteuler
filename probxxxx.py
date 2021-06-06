"""
Problem xxxx

"""

import argparse

def main(number, description, verbose = False):
    if description:
        print(__doc__)
    return number

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('-d','--description', action='store_true', default=False)
    args = parser.parse_args()
    sol = main(**vars(args))
    print(f'Solution: {sol}')
