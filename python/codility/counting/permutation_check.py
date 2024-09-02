

def solution(A):
    if not A:
        return 0
    maxVal = max(A)
    numSet = set()
    for n in A:
        if n not in numSet:
            numSet.add(n)
        else:
            return 0
    return 1 if len(numSet) == maxVal else 0


# Optimal Approach 

def solution_opt(A):
    N = len(A)
    expected_sum = N * (N + 1) // 2  # Sum of first N natural numbers
    actual_sum = sum(A)
    
    # Use a set to check for uniqueness
    if actual_sum != expected_sum or len(set(A)) != N:
        return 0
    
    return 1

