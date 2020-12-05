def solution(n, delivery):
    answer = ["?" for i in range(n)]

    for item in delivery:
        status = item[2]
        if status:
            # 보낸경우
            answer[item[0]-1] = "O"
            answer[item[1] - 1] = "O"
            continue
        else:
            # 못보낸경우
            if answer[item[0]-1] == "O" or answer[item[0]-1] == "?":
                answer[item[1] - 1] = "X"
            elif answer[item[1]-1] == "O" or answer[item[1]-1] == "?":
                answer[item[0] - 1] = "X"



    print(''.join(answer))
    # answer = ''
    return ''.join(answer)


# O?O?X?
solution(6, [[1, 3, 1], [3, 5, 0], [5, 4, 0], [2, 5, 0]])
# O?O?XXO
solution(7, [[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]])
