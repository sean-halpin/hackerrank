def solution(A):
    l = len(A)
    nums = set(list(range(1, l+1+1)))
    for n in A:
        nums.remove(n)
    return nums.pop()