# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    a = []
    answer = []
    strings.sort()

    for i in strings:
        # print(i[n])
        a.append(i[n])

    a.sort()

    for i in a:
        for j in range(len(a)):
            # print(strings[j][n])
            if i == strings[j][n]:
                answer.append(strings[j])
                # print(strings[j])
                strings[j] = '0'*100
                # print(strings[j])

    return answer

    # return sorted(sorted(strings), key=lambda strings: strings[n])
