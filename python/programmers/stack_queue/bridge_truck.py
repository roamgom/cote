# https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0 for i in range(bridge_length)]
    on_bridge_weight = []

    while truck_weights or sum(on_bridge) != 0:
        # 트럭 다리 건너기
        finished_truck = on_bridge.pop(0)
        if on_bridge_weight and on_bridge_weight[0] == finished_truck:
            # 지나간 트럭은 제거
            on_bridge_weight.pop(0)
        on_bridge.append(0)
        # 다음트럭 넣기
        if on_bridge[-1] == 0 and truck_weights:
            if sum(on_bridge_weight) + truck_weights[0] <= weight:
                # 무게 체크를 다리 상태가 아닌 따로 모아둬서 값 비교
                # 무게를 초과하면 skip
                truck = truck_weights.pop(0)
                on_bridge[-1] = truck
                on_bridge_weight.append(truck)
        answer += 1
    print(answer)
    return answer
    #
    # length = 0
    # while length < len(truck_weights):
    #     answer += 1
    #
    #     on_bridge.pop(0)
    #     if sum(on_bridge) + truck_weights[length] <= weight:
    #         # TODO: on_bridge의 sum() 시간복잡도 해결
    #         on_bridge.append(truck_weights[length])
    #         length += 1
    #     else:
    #         on_bridge.append(0)
    # print(answer)
    # return answer + bridge_length





solution(2, 10, [7,4,5,6])