# Boyle-Moore Voting Algorithm: This algorithm finds a candidate for the dominator in O(N) time.

def solution(A):
    N = len(A)
    if N <= 1:
        return -1

    count = 0
    candidate = None
    # Check who has more votes
    for c in A:
        if count == 0:
            candidate = c
            count += 1
        elif c == candidate:
            count += 1
        else:
            count -= 1

    if candidate is not None:
        tally = A.count(candidate)
        # Check is its dominant as per reqs
        if tally > (N // 2):
            return A.index(candidate)

    return -1

