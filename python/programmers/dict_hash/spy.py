# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter


def solution(clothes):
    result = 1
    counter_clothes = Counter([category for name, category in clothes])
    for cloth_counter in counter_clothes.keys():
        # 입지 않은 경우도 카운트해야하기 때문에 1 더함
        result *= (counter_clothes[cloth_counter]+1)

    result -= 1
    return result

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
