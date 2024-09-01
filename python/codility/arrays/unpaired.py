def solution(A):
    if not A:
        return 0
    pair_map = {}
    for e in A: 
        if e in pair_map and not pair_map[e]:
            pair_map[e] = True
        else: 
            pair_map[e] = False
    unpaired = [key for key,val in pair_map.items() if val == False]
    if unpaired:
        return unpaired[0]
    else: 
        return 0