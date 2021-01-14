# 소수 찾기

def solution(n):
    a = [False, False] + [True] * (n-1)
    primes = []

    for i in range(2, n+1):
        # print(a[i])
        if a[i]:
            primes.append(i)
            # print("1", 2*i,n+1,i)

            for j in range(2*i, n+1, i):
                # print(j)
                # print(a[j])
                a[j] = False

    return len(primes)
