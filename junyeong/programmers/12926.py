def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        else:
            a = ord(c)
            if ord(c) < 91:
                answer += chr(((a + n - 1) - 64) % (90 - 64) + 65)
            else:
                answer += chr(((a + n - 1) - 96) % (122 - 96) + 97)
    return answer
