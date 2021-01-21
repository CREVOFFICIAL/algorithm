# 스킬트리

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:

        #        기준이 되는 스킬 배열 만들기
        skill_list = list(skill)
        for s in skills:
            # print(s)
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
    return answer
