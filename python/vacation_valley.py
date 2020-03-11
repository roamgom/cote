# Problem link
# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    # n - 횟수
    # s - UDUD
    valley_count = 0
    height = 0
    for i in s:
        if i == 'U':
            height += 1
            if height == 0:
                valley_count += 1
        elif i == 'D':
            height -= 1
        else:
            print('error')
            return
    return valley_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    #
    # s = input()

    n = 8
    s = 'UDDUDUU'

    result = countingValleys(n, s)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
