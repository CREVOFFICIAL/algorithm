def solution(pre_skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_log = ''
        for skill in skill_tree:
            if skill in pre_skill:
                skill_log += skill
                
        if pre_skill.startswith(skill_log):
            answer += 1
        
    return answer
