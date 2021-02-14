#  제일 작은 수 구하기
def solution(arr):
  #  초반에는 이렇게 풀었는데
  # 테스트 케이스는 통과, 제출에서 오류
    #     arr.sort(reverse=True)
    #     tmp = arr[:-1]
    #     if not tmp:
    #       return [-1]
    #     else:
    #         return tmp

    arr.remove(min(arr))
    return arr if arr else [-1]
