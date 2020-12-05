# counting elements
# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

# 간단설명: N개 만큼의 카운터 배열(0초기화)을 만들고 A의 elem 값에 맞는 n-1 위치(ex: A[i]=1 -> cnt[0])
# 만약 A 요소값이 N+1 이면 전체 요소를 최댓값으로 바꾸고, 아닐경우 각 카운터+=1, 최대 카운터 수는 계속 업데이트
# score: 88% (corr: 100%, perform: 80%)

def solution(N, A):
    # O(N*M)
    # N - 숫자 카운터 갯수
    # A - 카운트용 숫자 조합
    counters = [0] * N

    max_count = 0

    # 3가지
    # 1. counter += 1 : 아무 조건 성립 없을 때
    # 2. max_count 업데이트
    # 3. 모든 카운터 max_count로 업데이트 (i==N+1)


    for i in A:
        if i == N+1:
            # M
            counters = [max_count] * N
            continue

        counters[i-1] += 1

        if counters[i-1] > max_count:
            # max_count 업데이트
            max_count = counters[i-1]

    return counters


def solution(N, A):
    # score: 88% (1 performance failed)
    # O(N+M)
    # N - 숫자 카운터 갯수
    # A - 카운트용 숫자 조합
    counters = [0] * N

    max_count = 0

    # 3가지
    # 1. counter += 1 : 아무 조건 성립 없을 때
    # max_count 업데이트
    # 2. 모든 카운터 max_count로 업데이트 (i==N+1)

    for i in A:
        # i == N+1 or i <= N
        if i <= N:
            counters[i-1] += 1
            if counters[i-1] > max_count:
                # max_count 업데이트
                max_count = counters[i-1]
        else:
            counters = [max_count] * N

    return counters


def solution(N, A):
    # score: 100%
    # O(N+M)

    counters = N * [0]
    next_max_counter =  max_counter = 0

    for oper in A:
        if oper <= N:
            current_counter = counters[oper-1] = max(counters[oper-1] +1, max_counter+1)
            next_max_counter = max(current_counter, next_max_counter)
        else:
            max_counter = next_max_counter

    return [c if c > max_counter else max_counter for c in counters]