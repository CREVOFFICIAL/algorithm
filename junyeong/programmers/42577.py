def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        for phone_number in phone_book[i+1:]:
            if phone_number.startswith(phone_book[i]):
                return False
    return True
