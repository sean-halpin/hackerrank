# O(1)

def solution(X, Y, D):
    return ((Y - X) // D) + (1 if ((Y - X) % D) != 0 else 0)

