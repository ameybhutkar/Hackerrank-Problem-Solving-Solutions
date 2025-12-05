# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import sys

def can_stack(cubes):
    dq = deque(cubes)
    prev = 10**18  # a very large number (works as "infinity")
    while dq:
        left = dq[0]
        right = dq[-1]
        # both ends are possible
        if left <= prev and right <= prev:
            # pick the larger one to be greedy (leave more room later)
            if left >= right:
                prev = dq.popleft()
            else:
                prev = dq.pop()
        elif left <= prev:
            prev = dq.popleft()
        elif right <= prev:
            prev = dq.pop()
        else:
            return False
    return True

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        cubes = [int(next(it)) for _ in range(n)]
        out_lines.append("Yes" if can_stack(cubes) else "No")
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
