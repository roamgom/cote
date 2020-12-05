# Problem link
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

from bisect import insort, bisect_left
import math
import os
import random
import re
import statistics
import sys


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    # TODO: median을 2개의 경우(홀,짝)으로 나누어 실행가능하게 만듬 (평균적으로 홀-1번, 짝-2번)

    # sorted 된 항목을 계속 사용하며 for loop 안에서
    # 사용한 값 (index)를 제거하고 다음 값을 추가
    sorted_expenditure = sorted(expenditure[:d])
    count = 0

    for index, value in enumerate(expenditure[d:]):
        # d 갯수 후의 값부터 계산 (median은 sorted_expenditure에 저장)
        de = expenditure[index]

        if d % 2 == 0:
            if value >= sorted_expenditure[d//2] + sorted_expenditure[d//2-1]:
                count += 1
        elif value >= sorted_expenditure[d//2] * 2:
            count += 1
        ix = bisect_left(sorted_expenditure, de)
        del sorted_expenditure[ix]
        insort(sorted_expenditure, value)
    #
    # for index in range(d, len(expenditure)):
    #     sorted_expenditure = sorted(expenditure[index-d:index])
        # expense = expenditure[index]
        # last_spent_expense = expenditure[index - d:index]
        # last_spent_expense_median = statistics.median(last_spent_expense)
        # print(f"day: {expense}")
        # print(f"spent: {last_spent_expense}")
        # print(f"median: {last_spent_expense_median}")
        # if expense >= last_spent_expense_median * 2:
        #     count += 1
        # if expenditure[index] >= statistics.median(sorted_expenditure) * 2:
        #     count += 1

    print(count)
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nd = input().split()

    # n = int(nd[0])
    n = 9

    # d = int(nd[1])
    d = 5

    # expenditure = list(map(int, input().rstrip().split()))
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

    result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    # fptr.close()
