# https://programmers.co.kr/learn/courses/30/lessons/42577

# Another
# def solution(phone_book):
#     sorted_phone_book = sorted(phone_book)
#
#     for ph, sorted_ph in zip(sorted_phone_book, sorted_phone_book[1:]):
#         if sorted_ph.startswith(ph):
#             return False
#     return True


def solution(phone_book):
    phone_book.sort()

    for phone_number in phone_book:
        index = phone_book.index(phone_number)
        for cmp_index in range(index + 1, len(phone_book)):
            if phone_number in phone_book[cmp_index]:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
