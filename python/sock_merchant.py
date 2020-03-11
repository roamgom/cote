# Problem link
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total = 0
    socks_set = set(ar)
    for socks in socks_set:
        socks_number = 0
        for position, item in enumerate(ar):
            if item == socks:
                socks_number += 1
        total += (socks_number // 2)
    print(total)
    return total
    # counter = Counter(ar)
    # return sum(socks_number // 2 for socks_number in counter.values())


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    n = 9
    # ar = list(map(int, input().rstrip().split()))
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()

