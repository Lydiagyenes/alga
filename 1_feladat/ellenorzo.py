#!/usr/bin/env python3

def icecreamParlor(m, arr):
    cost_map = {}
    for i, cost in enumerate(arr):
        diff = m - cost
        if diff in cost_map:
            return [cost_map[diff] + 1, i + 1]
        cost_map[cost] = i

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        m = int(data[idx])
        idx += 1
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+n]))
        idx += n
        result = icecreamParlor(m, arr)
        results.append(" ".join(map(str, result)))
    
    print("\n".join(results))
