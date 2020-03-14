# Problem link
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

# !/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0

    for i in range(1, len(s) + 1):
        # i: 글자수
        sorted_string = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]
        sorted_hash = Counter(sorted_string)
        # 글자 수를 고려하여 sort된 문자로 counter 생성

        for value in sorted_hash:
            # 조합의 갯수를 구한다
            # 2개 이상의 substring에서 짝수개 만큼만 적용
            # n*(n-1)/2
            count += (sorted_hash[value] * (sorted_hash[value] - 1)) / 2
    return int(count)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input())
    q = 2

    for q_itr in range(q):
        # s = input()
        s = "ifailuhkqq"

        result = sherlockAndAnagrams(s)

        # fptr.write(str(result) + '\n')

    # fptr.close()
