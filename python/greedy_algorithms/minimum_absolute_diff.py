# Problem link
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    minimum = abs(sorted_arr[0] - sorted_arr[1])
    for i in range(0, len(sorted_arr)-1):
        abs_diff = abs(sorted_arr[i] - sorted_arr[i+1])
        if minimum > abs_diff:
            minimum = abs_diff
    return minimum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # arr = list(map(int, input().rstrip().split()))
    arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]

    result = minimumAbsoluteDifference(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
