def solution(N):
    bin_str = format(N, 'b')
    cur = 0
    max = 0
    for c in bin_str:
        if c == "0":
            cur += 1
        elif c == "1":
            if cur > max:
                max = cur
            cur = 0
    return max