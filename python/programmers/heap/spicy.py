# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    mixed_count = 0
    # 매운 지수 오름차순 정렬
    while scoville[0] < K:
        if len(scoville) < 2:
            # 만약 K 이상의 지수가 안 나올경우
            return -1
        new_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_scoville)
        mixed_count += 1
    return mixed_count


solution([1, 2, 3, 9, 10, 12], 7)
solution([1, 2], 3)
