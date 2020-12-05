# https://programmers.co.kr/learn/courses/30/lessons/42746

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     # 1000 = 10^3
#     numbers.sort(key=lambda x:x*3, reverse=True)
#     # 숫자가 클 경우를 대비하여 str로 반환
#     return str(int(''.join(numbers)))


def solution(numbers):
    # 1~1000 -> 1,2,3,4의 최소공배수의 자리수로 맞춰준다
    # 1~100000
    numbers = list(map(str, numbers))
    answer = []
    com_list = []
    for number in numbers:
        if len(number) == 4:
            com_list.append([number, number * 3])
        elif len(number) == 3:
            com_list.append([number, number * 4])
        elif len(number) == 2:
            com_list.append([number, number * 6])
        elif len(number) == 1:
            com_list.append([number, number * 12])

    com_list.sort(key=lambda x:x[1], reverse=True)

    for i in com_list:
        answer.append(i[0])

    print("".join(answer))
    return str(int("".join(answer)))



solution([6, 10, 2])
solution([3, 30, 34, 5, 9])
