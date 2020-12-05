# Problem link
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count = 0
    for alphabet in range(97, 123):
        # 97 == ord('a')
        # 122 == ord('z')
        a_count = sum(letter == chr(alphabet) for letter in a)
        b_count = sum(letter == chr(alphabet) for letter in b)
        count += abs(a_count-b_count)
    # a_count = sum([letter for letter in a if ord('a') <= ord(letter) <= ord('z') and letter not in b])
    # b_count = sum([letter for letter in b if ord('a') <= ord(letter) <= ord('z') and letter not in a])
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a = input()

    # b = input()
    a = 'cde'
    b = 'abc'

    res = makeAnagram(a, b)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
