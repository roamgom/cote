# https://programmers.co.kr/learn/courses/30/lessons/42586

import math


def solution(progresses, speeds):
    answer = []
    days_spent = []
    for index in range(len(progresses)):
        days_spent.append(math.ceil((100 - progresses[index]) / speeds[index]))

    for index in range(1, len(days_spent)):
        if days_spent[index-1] > days_spent[index]:
            days_spent[index] = days_spent[index-1]

    tasks = 1
    for index in range(1, len(days_spent)):
        if days_spent[index-1] >= days_spent[index]:
            tasks += 1
        else:
            answer.append(tasks)
            tasks = 1

    # append last amount of tasks
    answer.append(tasks)

    return answer


solution([93, 30, 55, 60], [1, 30, 5, 40])
solution([93, 30, 55], [1, 30, 5])
solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7])
solution([93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7])


