def two_sum(nums, target):
    nums_hash = {}
    for i, n in enumerate(nums):
        diff = target-n
        if diff in nums_hash:
            return (nums_hash[diff], i)
        nums_hash[n] = i
        
print(two_sum([2,13,5,7,9], 14))