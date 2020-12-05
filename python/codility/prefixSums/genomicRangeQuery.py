# prefix sums
# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

# 간단설명: ACGT(1234) 에 맞춰 P,Q의 각 값에 맞는 index range에 
# score: 100%

def solution(S, P, Q):

    answers = []

    for i in range(len(P)):
        # O(N)
        nucleotide_slice = S[P[i]: Q[i]+1]
        # 여기를 개선
        # score: 50% (ac:100%, perform: 0%)
        # answers.append(nucleotide[min(nucleotide_slice)])

        # (M)
        if 'A' in nucleotide_slice:
            answers.append(1)
        elif 'C' in nucleotide_slice:
            answers.append(2)
        elif 'G' in nucleotide_slice:
            answers.append(3)
        else:
            answers.append(4)

        # 결론적으로 O(N+M)
    
    return answers