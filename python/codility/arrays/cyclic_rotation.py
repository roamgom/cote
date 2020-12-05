# arrays
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

# 간단설명: A list와 K를 받고 A 마지막 요소를 맨 앞으로 넣어 rotation을 진행
# score: 87%
# 원인: N, K는 0-100 사이의 integer 값이라 하였기 때문에 
# 빈 list에 대해 처리가 없어 runtime error 발생

def solution(A, K):
    # write your code in Python 3.6
    move_A = A
    for i in range(K):
        move_A.insert(0, move_A.pop(-1))

    return move_A


# 해결법
def solution(A, K):
    # write your code in Python 3.6
    if A:
        move_A = A
        for i in range(K):
            move_A.insert(0, move_A.pop(-1))

        return move_A
    else:
        return []