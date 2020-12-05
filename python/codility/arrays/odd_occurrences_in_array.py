# arrays
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

# 간단설명: 배열에서 하나의 다른 수를 제외하고 전부 2개 쌍으로 숫자가 있다.
# 하나의 숫자를 찾아서 출력하기
# score: 33%
# 원인: 아무래도 비교 부분에서 처리 못하는 경우가 발생해서 그런 것 같다
# 아래는 인터넷에서 찾은 해결책

def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    
    A.sort()
    
    for idx, num in enumerate(A):
        if(num == A[idx+1]):
            continue
        elif (num == A[idx-1]):
            continue
        else:
            return num
    

# 해결책
def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    
    A.sort()
    
    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        elif A[i] != A[i+1]:
            return A[i]
