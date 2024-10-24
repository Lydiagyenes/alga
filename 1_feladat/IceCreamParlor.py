#!/bin/python3

import os

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Create a dictionary to store the indices of costs we've seen
    cost_map = {}
    
    # Iterate over the list of costs
    for i, cost in enumerate(arr):
        diff = m - cost  # Calculate the difference
        
        # If the difference exists in cost_map, we've found the pair
        if diff in cost_map:
            # Return the indices in 1-based format
            return [cost_map[diff] + 1, i + 1]
        
        # Store the current cost with its index
        cost_map[cost] = i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Number of trips

    for t_itr in range(t):
        m = int(input().strip())  # Total money pooled

        n = int(input().strip())  # Number of flavors

        arr = list(map(int, input().rstrip().split()))  # List of costs

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
