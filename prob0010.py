def main(number):
    if number < 2:
        raise ValueError("The parsed number must be an integer greater or equal 2.")

    n = number

    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p * p, n, p):
                sieve[i] = False
    return sum

if __name__ == "__main__":
    sol = main(2000000)
    print(f'Solution: {sol}')
