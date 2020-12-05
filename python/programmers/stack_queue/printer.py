# https://programmers.co.kr/learn/courses/30/lessons/42587


def solution(priorities, location):
    index_priority_list = [(index, priority) for index, priority in enumerate(priorities)]

    task_queue = []

    while index_priority_list:
        index_priority = index_priority_list.pop(0)
        priority = index_priority[1]

        priority_list = [priority for index, priority in index_priority_list]

        if priority_list:
            max_priority = max(priority_list)

        if priority >= max_priority:
            task_queue.append(index_priority)
        else:
            index_priority_list.append(index_priority)

    print(task_queue)
    for index, priority in enumerate(task_queue):
        if priority[0] == location:
            return index + 1

    # return answer


solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)
