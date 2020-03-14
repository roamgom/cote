# Problem link
# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    count = 0
    total = 0
    price_list = sorted(prices)
    for index, value in enumerate(price_list):
        if total + value < k:
            total += value
            count += 1
    print(count)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])
    n = 7

    # k = int(nk[1])
    k = 50

    # prices = list(map(int, input().rstrip().split()))
    prices = [1, 12, 5, 111, 200, 1000, 10]

    result = maximumToys(prices, k)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
