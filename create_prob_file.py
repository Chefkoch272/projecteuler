import os
import argparse
import scraper

def main(problem_number):
    problem = scraper.problem(number=problem_number)
    f_name = 'prob' + str(problem_number).zfill(4) + '.py'
    f = open(f_name, 'x')
    # Todo: fill new file with template structure

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--problem_number', type=int)
    args = parser.parse_args()
    main(**vars(args))