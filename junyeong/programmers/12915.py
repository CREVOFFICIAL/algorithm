def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda word:word[n])
    return strings
