# prefix sums
# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

# 간단설명: A ~ B 사이 K로 나누어 떨어지는 숫자 갯수 구하기. B//K 에서 A//K를 빼고 A가 K로 나누어 떨어지면 갯수를 1개 추가해준다.
# score: 100%

def solution(A, B, K):
    # score: 50% (acc: 100%, perform: )
    count = (B//K) - (A//K)
    if (A % K == 0):
        count += 1
    return count
