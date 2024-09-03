def solution(A, B):
    N = len(A)
    downstream_fish = []
    survivors = 0
    for i in range(N):
        size = A[i]
        dir = B[i]
        if dir == 1:
            downstream_fish.append(size)
        elif dir == 0:
            if not downstream_fish:
                survivors += 1
            else:
                while downstream_fish:
                    if downstream_fish[-1] < size: # up fish wins
                        downstream_fish.pop()
                    else:
                        break
                if not downstream_fish:
                    survivors +=1
                
    return survivors + len(downstream_fish)