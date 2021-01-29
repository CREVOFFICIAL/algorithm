def solution(papers):
    paper_counts = dict()
    paper_indices = sorted(set(papers))
    
    for paper in papers:
        if paper in paper_counts:
            paper_counts[paper] += 1
        else:
            paper_counts[paper] = 1
    
    count = len(papers)
    most_referenced = max(papers)
    h_index = 0
    
    for index in range(most_referenced):
        if count >= index:
            h_index = index
        else:
            break
        if index in paper_counts:
            count -= paper_counts[index]
    return h_index
