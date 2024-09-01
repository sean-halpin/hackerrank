def solution(A):
    sum_A = sum(A)
    left_sum = 0
    min_abs = float('inf')
    for n in A[:-1]:
        left_sum += n
        abs_dif = abs(left_sum - (sum_A - left_sum))
        min_abs = min(min_abs, abs_dif)
    return min_abs