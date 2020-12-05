# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

import collections

def solution(participant, completion):
    answer = collections.Counter(completion) - collections.Counter(participant)
    return list(answer.keys())[0]

# print(solution(["leo", "kiki", "eden"], 
#          ["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], 
#          ["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"], 
#          ["stanko", "ana", "mislav"]))