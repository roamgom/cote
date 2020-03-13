# Problem link
# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    alphabet_count = 0
    alphabet_in_string = s.count('a')
    loop_number = n // len(s)
    alphabet_count += alphabet_in_string * loop_number
    remain_number = n % len(s)
    for index, alphabet in enumerate(s):
        if index < remain_number and alphabet == 'a':
            alphabet_count += 1

    return alphabet_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    #
    # n = int(input())

    s = 'aba'
    n = 10

    result = repeatedString(s, n)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
