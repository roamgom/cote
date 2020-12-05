# counting elements
# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

# 간단설명: 입력된 list 에서 연속된 단일 숫자로 이루어졌는지(permutation) 확인하여 맞을경우 1 아닐경우 0 반환
# 중복 또는 1로 시작하지 않을 경우 permutation 이 아니기 때문에 0 반환
# score: 100%

def solution(A):
    # O(NlogN + N)

    # NlogN
    A.sort()

    if A[0] != 1:
        return 0

    # N
    for i in range(len(A)-1):
        if A[i] + 1 != A[i+1] or A[i] == A[i+1]:
            return 0
    return 1