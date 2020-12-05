# iterations
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

# 간단설명: 입력된 10진수를 2진수로 표현하여 1 사이의 0 길이가 가장 긴걸 출력
# score: 100%

def solution(N):
    # write your code in Python 3.6
    bin_N = str(bin(N)[2:])
    one_index = [i for i, e in enumerate(bin_N) if e == '1']
    
    max_one_length = 0
    for i in range(len(one_index)-1):
        one_length = one_index[i+1]-one_index[i]-1
        if one_length > max_one_length:
            max_one_length = one_length
    
    return max_one_length