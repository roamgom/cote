# counting elements
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

# 간단설명: N 개 만큼의 리스트에 없는 최소 양수를 반환하시오
# score: 100%
# set은 hash 를 사용하기 때문에 list보다 시간복잡도가 더 낮다

def solution(A):
    # write your code in Python 3.6
    set_A = set(A)

    smallest = 1

    while True:
        if smallest in set_A:
            smallest += 1
        else:
            return smallest
