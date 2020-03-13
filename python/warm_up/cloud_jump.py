# Problem link
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # 1-0
    # 0-0
    number_of_jump = 0
    location = 0
    end = len(c)-1

    while location < end:
        if location+2 <= end and c[location + 2] == 0:
            location += 2
            number_of_jump += 1
        elif c[location + 1] == 0:
            location += 1
            number_of_jump += 1
    return number_of_jump


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    #
    # c = list(map(int, input().rstrip().split()))

    n = 7
    c = [0,0,0,0,0,1,0]

    result = jumpingOnClouds(c)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
