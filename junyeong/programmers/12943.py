def solution(num):
    count = 0
    while(count<500 or num != 1):
        if num == 1:
            return count
        num = num % 2 == 0 and num // 2 or num * 3 + 1
        count += 1
    else:
        return -1
