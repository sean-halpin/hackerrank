def maxSubArray(arr) -> int:
    curr_sum = arr[0]
    max_sum = arr[0]
    for n in arr[1:]:
        if curr_sum < 0:
            curr_sum = n
        else:
            curr_sum = curr_sum + n
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
