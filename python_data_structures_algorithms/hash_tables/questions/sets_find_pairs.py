def find_pairs(l1, l2, t):
    seen = set()
    pairs = []
    for n in l1:
        seen.add(n)
    for n in l2:
        if t-n in seen:
            pairs.append((t-n, n))
    return pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""