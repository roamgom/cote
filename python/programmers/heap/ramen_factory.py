# https://programmers.co.kr/learn/courses/30/lessons/42629

import collections


def solution(stock, dates, supplies, k):
    # stock - 재고
    # dates - 공급 일정
    # supplies - 공금 가능
    # k - 공급 시점
    answer = 0
    need = []
    dates_deque = collections.deque(dates)
    supplies_deque = collections.deque(supplies)
    while stock < k:
        # stock이 k 이상이면 문제 없음
        while len(dates_deque) > 0 and dates_deque[0] <= stock:
            # 필요한 물자 수 체크
            # TODO: list의 경우 pop(0)을 쓰면 O(N)의 시간복잡도
            # collections.deque를 사용하면 복잡도가 O(1)
            # heapq.heappop(dates)
            dates_deque.popleft()
            # need.append(heapq.heappop(supplies))
            need.append(supplies_deque.popleft())

        max_supply = max(need)
        need.remove(max_supply)
        stock += max_supply
        answer += 1

    # print(answer)
    return answer



solution(4, [4, 10, 15], [20, 5, 10], 30)
