def main(n_divisors, n_tri_max):
    n = 1
    n_tri = 0

    while True:
        if n_tri_max > 0 and n > n_tri_max:
            break

        n_tri = n_tri + n

        divisors = get_divisors(n_tri)
        if len(divisors) >= n_divisors:
            return n_tri, divisors

        if n % 10 == 0:
            print(n)

        n += 1

def get_divisors(n):
    divisors = []

    for i in range(1, int(n**.5)):
        if round(n/i) == n/i:
            divisors += [i, int(n/i)]

    return divisors

if __name__ == '__main__':
    solution = main(n_divisors=500, n_tri_max=0)
    print(*solution)