# Problem link
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    largest_value = -63
    size = len(arr[0]) - 1

    for row in range(1, size):
        for col in range(1, size):
            numbers = []
            numbers += [arr[row][col]]
            numbers += arr[row-1][col-1:col+2]
            numbers += arr[row+1][col-1:col+2]
            cube = sum(numbers)
            if cube > largest_value:
                largest_value = cube
    return largest_value

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    # arr = [[1, 1, 1, 0, 0, 0],
    #        [0, 1, 0, 0, 0, 0],
    #        [1, 1, 1, 0, 0, 0],
    #        [0, 0, 2, 4, 4, 0],
    #        [0, 0, 0, 2, 0, 0],
    #        [0, 0, 1, 2, 4, 0]]

    arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]

    result = hourglassSum(arr)

    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
