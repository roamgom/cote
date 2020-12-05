def solution(id_list, k):
    # 발행한 티켓 수
    answer = 0
    id_count = {}
    for ids in id_list:
        for user_id in set(ids.split()):
            # 같은 구매여도 1개로 취급하여 set으로 변환
            if user_id in id_count:
                if id_count[user_id] < k:
                    id_count[user_id] += 1
            else:
                id_count[user_id] = 1


    # print(id_count)
    # print(sum(id_count.values()))
    return sum(id_count.values())


solution(["A B C D", "A D", "A B D", "B D"], 2)
solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3)
