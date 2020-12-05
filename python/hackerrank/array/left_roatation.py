# Problem link
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    array = a
    for i in range(d):
        array.append(array.pop(0))
    return array


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    # n = int(nd[0])
    #
    # d = int(nd[1])
    #
    # a = list(map(int, input().rstrip().split()))

    n = 5
    d = 4
    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
