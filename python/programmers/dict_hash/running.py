# https://programmers.co.kr/learn/courses/30/lessons/42576
import collections


# .count는 효율이 안나옴
# def solution(participant, completion):
#     answer = ''
#     for i in participant:
#         if participant.count(i) > completion.count(i):
#             answer = i
#     return answer

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"],
         ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
         ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],
         ["stanko", "ana", "mislav"]))
