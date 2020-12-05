# https://programmers.co.kr/learn/courses/30/lessons/42839

import itertools


def solution(numbers):
    # 조합으로 순열 만들기
    case = []
    for i in range(1, len(numbers)+1):
        case.append(set(map(int, map(''.join, itertools.permutations(numbers[:i])))))
    case = set(itertools.chain(*case))

    for number in case:
        for n in range(2, number+1):
            if number % n == 0:
                break
        




    print(case)
    answer = 0
    return answer



solution("17")
solution("011")
