# 전화번호 목록

# 해시 문제, tri라는 자료구조도 가능

def solution(phone_book):
    phone_book.sort()

    for number in phone_book:
        # print(number)
        for i in range(len(phone_book)-1):
            # print(phone_book[i+1])
            if number in phone_book[i+1]:
                # print(phone_book[i])
                return False
            else:
                return True
