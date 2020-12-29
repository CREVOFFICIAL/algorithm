# 완주하지 못한 선수

def solution(participant, completion):
    # print("1",participant)
    participant.sort()
    completion.sort()
    # print("2", participant)
    # print("2", completion)

    for p, c in zip(participant, completion):
        # test = list(zip(participant, completion))
        # print(test)
        # print(p, c)
        if p != c:
            return p
    return participant.pop()
