# time complexity
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

# 간단설명: 배열을 iterate 하며 한 elem 기준으로 앞뒤 list slice한 값 합 차이의 절대값 중 최솟값 반환
# score: 53% (corr:100%, perform: 0%)

def solution(A):
    # time complex: O(N^2)
    min_dist = 0
    
    # O(N)
    for i in range(1, len(A)):
        # O(N)
        front = sum(A[:i])
        back = sum(A[i:])
        if abs(front-back) < min_dist:
            min_dist = abs(front-back)
    return min_dist


# score: 100%
def solution(A):
    front = 0
    # O(N)
    back = sum(A)
    min_diff = 2000

    # O(N)
    for i in range(1, len(A)):
        front += A[i-1]
        back -= A[i-1]

        diff = abs(front-back)

        if diff < min_diff:
            min_diff = diff

    return min_diff
