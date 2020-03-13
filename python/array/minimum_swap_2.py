# Problem link
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    temp_array = {value: index for index, value in enumerate(arr)}
    swap_count = 0

    for i in range(len(arr)):
        actual_value, expected_value = arr[i], i + 1
        actual_index, expected_index = i, temp_array[expected_value]
        if actual_value != expected_value:
            arr[actual_index] = expected_value
            arr[expected_index] = actual_value
            temp_array[actual_value] = expected_index
            temp_array[expected_value] = actual_index
            swap_count += 1
    return swap_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
