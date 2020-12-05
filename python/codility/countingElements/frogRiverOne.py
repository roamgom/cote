# counting elements
# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

# 간단설명: X 수만큼의 나뭇잎 배열을 할당 A 배열에 맞게 나뭇잎 배열이 채워짐 다 채워질 때의 A idx 가 개구리가
# 건널 수 있는 최솟 값 구하기
# score: 53% (corr: 100%, perform: 0%)

def solution(X, A):
    # O(N**2)
    # write your code in Python 3.6
    leaves = [0 for i in range(X)]

    # N
    for idx, pos in enumerate(A):
        leaves[pos-1] = 1
        # N
        if len(set(leaves)) == 1:
            return idx
    return -1


# score: 100%
def solution(X, A):
    # O(N)
    leaves = [0 for i in range(X)]
    leaves_count = 0

    # N
    for idx, pos in enumerate(A):
        if leaves[pos-1] == 0:
            leaves[pos-1] = 1
            leaves_count += 1

            if leaves_count == X:
                return idx

    return -1