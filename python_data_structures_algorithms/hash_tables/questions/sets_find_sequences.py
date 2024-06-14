def longest_consecutive_sequence(l1):
    if len(l1) == 0:
        return 0
    max = 1
    seen = set()
    curr_seq = 0
    for n in l1:
        seen.add(n) if n not in seen else None
    for s in seen:
        curr_seq = 1
        # print(s, curr_seq, s+curr_seq)
        while (s+curr_seq) in seen:
            curr_seq += 1
            if curr_seq > max:
                max = curr_seq
    return max

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""