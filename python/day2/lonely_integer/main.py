def lonely_integer(arr):
    hashmap = dict() # or hashmap = {}
    for i in arr:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    keys = [(key) for key, value in hashmap.items() if value == 1]
    return keys[0]

arr = [1,2,3,4,3,2,1]
print(lonely_integer(arr))
