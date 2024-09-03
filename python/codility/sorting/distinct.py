def solution(A):
    if not A:
        return 0
    A.sort()
    acc = 0
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            acc += 1
    return acc + 1

# O(N*log(N)) - due to .sort being dominant operation
# strategy here is to sort the array in place, then count the number of pairs that are different
