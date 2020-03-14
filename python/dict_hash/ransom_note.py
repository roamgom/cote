# Problem link
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    """
    노트에 담긴 단어들과 잡지의 단어 수를 비교하여
    노트의 단어 수가 잡지의 단어로 표현이 가능하면 Yes
    갯수 또는 단어가 표현 불가할 경우 No

    Python collection의 Counter를 사용하여
    Hash table인 dict를 생성 후, 노트의 키워드 수가
    잡지의 키워드 수보다 크거나 단어가 없으면 수용불가(No)
    아닐경우 수용가능(Yes)
    :param magazine: 잡지(비교용)
    :param note: Ransom 노트
    :return:
    """
    magazine_counter = Counter(magazine)
    note_counter = Counter(note)

    for keyword in note_counter:
        if note_counter[keyword] > magazine_counter[keyword]:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    # mn = input().split()

    # m = int(mn[0])
    m = 6

    # n = int(mn[1])
    n = 5

    # magazine = input().rstrip().split(' ')
    magazine = "two times three is not four"

    # note = input().rstrip().split(' ')
    note = "two times two is four"

    checkMagazine(magazine, note)
