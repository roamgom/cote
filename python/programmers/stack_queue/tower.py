# https://programmers.co.kr/learn/courses/30/lessons/42588


def solution(heights):
    answer = []
    value = 0

    # 큐 개념으로 풀이
    # 가장 왼쪽 타워는 수신 불가 0 처리
    max_height = heights[0]
    answer.append(value)

    for i in range(1, len(heights)):
        if heights[i] > max_height:
            max_height = heights[i]
            value = 0
        if heights[i] < heights[i - 1]:
            value = i
        answer.append(value)

    # print(answer)
    return answer


solution([6, 9, 5, 7, 4])
solution([3, 9, 9, 3, 5, 7, 2])
solution([1, 5, 3, 6, 7, 6, 5])
