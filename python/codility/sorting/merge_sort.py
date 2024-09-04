def merge_sort(A):
    if len(A) == 1:
        return A
    midpoint = len(A) // 2
    left = A[:midpoint]
    right = A[midpoint:]
    l_sorted = merge_sort(left)
    r_sorted = merge_sort(right)
    return merge(l_sorted, r_sorted)

def merge(A,B):
    LA = len(A)
    LB = len(B)
    i = 0
    j = 0
    res = []
    while i < LA and j < LB:
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    # print(i,j,LA,LB,A[i:], B[j:])
    if i < LA:
        res = res + A[i:]
    elif j < LB:
        res = res + B[j:]
    return res