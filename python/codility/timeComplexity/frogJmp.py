# time complexity
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

# 간단설명: 
# score: 100%

def solution(X, Y, D):
    # write your code in Python 3.6

    if D > Y:
        return 0

    if (Y-X) % D == 0:
        return (Y-X) // D
    return (Y-X) // D + 1