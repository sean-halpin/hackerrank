def solution(A, K):
    if not A:
        return A
    L = len(A)
    shift = L - (K % L)
    return A[shift:] + A[:shift]