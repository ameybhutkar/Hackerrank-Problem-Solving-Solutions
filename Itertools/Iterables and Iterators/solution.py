# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import comb

n = int(input().strip())
letters = input().split()         # list of n lowercase letters
k = int(input().strip())

c = letters.count('a')            # number of 'a' in the list

# If choosing k from the n-c non-'a' is impossible, probability = 1
if n - c < k:
    prob = 1.0
else:
    prob = 1.0 - comb(n - c, k) / comb(n, k)

print(prob)
