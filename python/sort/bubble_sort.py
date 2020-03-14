# Problem link
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    """
    2중 for 문 쓰는것보다 while loop 안에서 상태 체크를 하며
    숫자 오림차순으로 바꾸기
    :param a: unsorted array
    :return:
    """
    count = 0

    while True:
        finished = True
        for index in range(len(a)-1):
            if a[index] > a[index+1]:
                a[index], a[index+1] = a[index+1], a[index]
                count += 1
                finished = False

        if finished:
            break

    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    # n = int(input())
    n = 3

    # a = list(map(int, input().rstrip().split()))
    a = [3, 2, 1]

    countSwaps(a)
