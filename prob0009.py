def main(number, verbose=False):
    solution = []

    for c in range(number+1):
        c_diff = number - c
        for b in range(c_diff+1):
            a = c_diff - b
            if a < b and b < c:
                if verbose:
                    print(c, b, a)
                if a**2 + b**2 == c**2:
                    solution.append(a * b * c)

    return solution

if __name__ == "__main__":
    sol = main(1000)
    print(f'Solution: {sol}')
