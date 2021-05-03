# 땅따먹기

def solution(land):
    n = len(land)-1
    # print(n)
    for i in range(n):
        print('i', i)
        print(land[i+1][0])
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[n][0], land[n][1], land[n][2], land[n][3])
