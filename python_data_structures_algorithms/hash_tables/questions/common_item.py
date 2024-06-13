def item_in_common(l1, l2):
    hash_table = {}
    for c in l1:
        hash_table[c] = True
    for c in l2:
        if hash_table.get(c):
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))

"""
    EXPECTED OUTPUT:
    ----------------
    True

"""