# 큰 수 만들기
# 완전탐색과 백트래킹을 이용하는 거라는데 잘 이해가 가지 않는다
def solution(number, k):
    collected = []

    for i, num in enumerate(number):
        # print(i, num)

        while len(collected) > 0 and collected[-1] < num and k > 0:
            # print("collected", collected)
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    # print(collected)
    return ''.join(collected)
