import pandas as pd

def main(n_max, verbose=False):
    series = pd.DataFrame(range(1,n_max+1))
    square_of_sum = (series.sum()**2)[0]
    sum_of_squares = ((series * series).sum())[0]
    if verbose:
        print(f'{square_of_sum} - {sum_of_squares} equals following solution.')
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    sol = main(100)
    print(f'Solution: {sol}')