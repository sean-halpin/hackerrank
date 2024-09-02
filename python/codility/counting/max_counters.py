def solution(N, A):
    counters = [0] * N
    curr_max = 0
    prev_max_op = 0
    for num in A:
        if num > 0 and num <= N:
            if counters[num-1] < prev_max_op:
                counters[num-1] = prev_max_op
            counters[num-1] += 1
            curr_max = max(counters[num-1],curr_max)
        if num > N:
            prev_max_op = curr_max
    for i in range(len(counters)):
        if counters[i] < prev_max_op:
            counters[i] = prev_max_op
    return counters