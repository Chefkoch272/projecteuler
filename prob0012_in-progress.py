def return_divisors(n):
    '''Returns list of all divisors'''
    divisors = []
    # Todo: Check if there's a pattern, based on which numbers can be skipped
    for m in range(1,n+1):
        if n % m == 0:
            divisors.append(m)
    return divisors

def main(n):
    print(f'Searching for first number with {n} divisors...')

    n_divisors = 0
    i = 0

    # TODO NEXT: only take triangular numbers into account.
    # Todo: Check if there's a pattern, based on which numbers can be skipped
    while n_divisors < n:
        i += 1
        divisors = return_divisors(i)
        if len(divisors) > n_divisors:
            n_divisors = len(divisors)
        if i % 1000 == 0:
            print('Iteration number: ', i)

    print(f'{i} is the first number with {n} divisors.')

if __name__ == '__main__':
    main(n=30)