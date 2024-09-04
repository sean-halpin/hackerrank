def solution(A):
    # A=[5,2,3,4,1,4] , solution = days(buy,sell idx) [4,5], prices [1,4], profit 3
    # step 1: i = 0
    # min=5, max=5, prof=(5-5)=0
    # step 2: i = 1
    # min=2, max=0, prof=0
    # step 3: i = 2
    # min=2, max=3, prof=1
    if not A:
        return 0

    minim = float('inf')
    maxim = 0
    prof = maxim - minim
    for n in A:
        if n < minim:
            minim = min(minim, n)
            maxim = minim
        if n > maxim:
            maxim = max(maxim, n)
        prof = max(prof, maxim - minim)
    return prof