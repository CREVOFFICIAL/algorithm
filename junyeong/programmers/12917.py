def solution(s):
    letters = list(s)
    letters.sort(reverse=True)
    return ''.join(letters)
