"""
Ideas:
- create lookup table once terms are detected which have been in earlier terms
  -> can be based on dict in which the key is the first term of the sub-chain
- create array with objects for which a method to find their chains is applied simultaneously
"""

def apply_odd(n):
    return n/2

def apply_even(n):
    return 3*n +1

def next_term(n):
    if n % 2:
        return apply_even(n)
    else:
        return apply_odd(n)

longest_chain = []
n_max = 1000000
for i in range(1, n_max + 1):
    j = i
    chain = []
    while True:
        chain.append(j)
        if j == 1:
            break
        j = next_term(j)
    if len(chain) > len(longest_chain):
        longest_chain = chain

print('Starting number ', longest_chain[0], 'produces length ', len(longest_chain))
# print(longest_chain)
