import help_functions

def main(number):
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
    sol = main(10001)
    print(f'Solution: {sol[-1]}')