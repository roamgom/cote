import itertools
import math

# conditional combination 문제 인듯

def solution(n, m, k):
    # TODO: n의 조합법 구하기 - 스키/보드 슬로프 조합
    # TODO: 합이 m/2이며 k보다 작거나 같은 숫자의 중복조합 구하기
    # Factorial로 경우의 수 구하기?
    # 둘이 곱하면 경우의 수
    # n - 슬로프 갯수
    # m - 산 너비
    # k - 길이 제한
    answer = -1

    if n > m or m // n > k:
        # 슬로프 수(n)이 폭(m)보다 크면 조합 불가
        # 폭을 수로 나눈 평균 길이가 제한 길이보다 크면 불가
        # 설계 불가능한 슬로프
        return 0

    # 각 슬로프의 길이의 조합 가지
    # TODO: 시간이 너무 오래 걸림 (+ filter 부분)
    combination = list(itertools.combinations_with_replacement(range(1, k+1), n))

    # print(combination)
    possible = list(filter(lambda x: sum(x) == m, combination))
    print(possible)
    # print(math.factorial(len(possible)))
    answer = math.factorial(len(possible))
    # print(n, m, k)
    return answer % 1000000007


# 6
solution(3, 8, 4)
# 0
solution(10, 6, 5)
# 0
solution(2, 10, 4)
# 시간이 너무 오래걸림
# 780361386
# solution(50, 150, 20)
