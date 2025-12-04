# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
import sys

k, m = map(int, sys.stdin.readline().split())
lists = []
for _ in range(k):
    parts = list(map(int, sys.stdin.readline().split()))
    lists.append(parts[1:])   # first number is the count, remaining are the elements

# compute maximum of (sum(x*x) % m) over Cartesian product of choices
result = max(sum(x*x for x in comb) % m for comb in product(*lists))
print(result)
