#!/bin/python3
from collections import Counter

if __name__ == '__main__':
    s = input()
# Count characters
count = Counter(s)
# Sort by:
# 1. Highest frequency (descending)
# 2. Alphabetical order (ascending)
result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

# Print top 3
for char, freq in result[:3]:
    print(char, freq)

