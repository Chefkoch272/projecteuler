def main(p):
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
    sol, _ = main(600851475143)
    print(f'Solution: {sol}')