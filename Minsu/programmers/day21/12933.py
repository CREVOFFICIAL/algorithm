# 정수 내림차순으로 배치
# int -> str 형태로 바꿔줘야 list 가능
def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int("".join(ls))
