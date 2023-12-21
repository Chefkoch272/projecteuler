import pandas as pd

def main(n_max):
    df = pd.DataFrame()
    df['fib'] = fib(n_max=n_max)
    df['even'] = is_divisible(df['fib'], 2) * df['fib']
    return df['even'].sum(), df

def fib(n_max):
    m = 1
    n = 1
    fib_list = []

    while n <= n_max:
        fib_list.append(n)
        _ = n
        n = m + n
        m = _
    return fib_list

def is_divisible(number, divisor):
    return (number % divisor == 0)

if __name__ == '__main__':
    sol, _ = main(4000000)
    print(f'Solution: {sol}')


