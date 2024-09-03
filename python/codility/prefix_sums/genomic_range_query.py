def solution(S, P, Q):
    ls = len(S)
    lp = len(P)

    occ_a = [0] * (ls + 1)
    occ_c = [0] * (ls + 1)
    occ_g = [0] * (ls + 1)
    occ_t = [0] * (ls + 1)

    for i in range(1, ls + 1):
        occ_a[i] = occ_a[i - 1] + (1 if S[i-1] == "A" else 0)
        occ_c[i] = occ_c[i - 1] + (1 if S[i-1] == "C" else 0)
        occ_g[i] = occ_g[i - 1] + (1 if S[i-1] == "G" else 0)
        occ_t[i] = occ_t[i - 1] + (1 if S[i-1] == "T" else 0)
    # print(occ_a, occ_c, occ_g, occ_t)
    results = []
    for i in range(lp):
        # print(i)
        if occ_a[1 + Q[i]] - occ_a[P[i]] > 0:
            results.append(1)
        elif occ_c[1 + Q[i]] - occ_c[P[i]] > 0:
            results.append(2)
        elif occ_g[1 + Q[i]] - occ_g[P[i]] > 0:
            results.append(3)
        elif occ_t[1 + Q[i]] - occ_t[P[i]] > 0:
            results.append(4)
        # print(results)
    
    return results


