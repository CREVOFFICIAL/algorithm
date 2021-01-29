def solution(x):
    digits = list(str(x))
    all_digits_sum = 0
    for digit in digits:
        all_digits_sum += int(digit)
    
    return x % all_digits_sum == 0
