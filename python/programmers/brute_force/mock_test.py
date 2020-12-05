# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    answer_one = [1, 2, 3, 4, 5] # 5개
    answer_two = [2, 1, 2, 3, 2, 4, 2, 5] # 8개
    answer_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개
    answer = [0, 0, 0]

    # for index, answer in enumerate(answers):
    #     if answer == answer_one[index%5]:
    #         answer[0] += 1
    #     if answer == answer_two[index % 8]:
    #         answer[1] += 1
    #     if answer == answer_three[index % 10]:
    #         answer[2] += 1

    answer_count = [
        len([1 for index in range(len(answers)) if answers[index] == answer_one[index%5]]),
        len([1 for index in range(len(answers)) if answers[index] == answer_two[index%8]]),
        len([1 for index in range(len(answers)) if answers[index] == answer_three[index%10]]),
    ]
    print(answer_count)
    answer = [index+1 for index in range(3) if answer_count[index] == max(answer_count)]
    print(answer)
    return answer


solution([1,2,3,4,5])