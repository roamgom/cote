# time complexity
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

# 간단설명: N -> 1~N+1 배열에서 1개의 요소가 빠진 배열 생성. 빠진 요소 return
# score: 100%

def solution(A):
    # write your code in Python 3.6
    set_A = set(A)
    max_A = len(A) + 1
    compare_A = set(range(1, max_A+1))
    return list(compare_A - set_A)[0]