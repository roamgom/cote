# Problem link
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    minus_one_list = [value-1 for value in q]

    for i, value in enumerate(minus_one_list):
        if value - i > 2:
            print("Too chaotic")
            return

        for j in range(max(value-1, 0), i):
            if minus_one_list[j] > value:
                count +=1
    print(count)

    # count = 0
    # init_list = sorted(q)
    # for value in q:
    #     if init_list.index(value) - q.index(value) > 2:
    #         print("Too chaotic")
    #         return
    #
    # while True:
    #     if init_list == q:
    #         break
    #     dump = None
    #     for index, value in enumerate(init_list):
    #         if q[index] == init_list[index - 1] and (
    #                 init_list[index] == q[index - 1] or init_list[index] == q[index - 2]):
    #             dump = init_list[index - 1]
    #             init_list[index - 1] = init_list[index]
    #             init_list[index] = dump
    #             count += 1
    # print(count)


if __name__ == '__main__':
    # t = int(input())
    t = 2

    for t_itr in range(t):
        # n = int(input())
        n = 5

        # q = list(map(int, input().rstrip().split()))
        q = [2, 1, 5, 3, 4]

        result = minimumBribes(q)
