arr = [ [1,2,3],
        [4,5,6],
        [9,8,9]]

def diag_diff(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr[0])):
        sum1 += arr[i][i]
        sum2 += arr[i][len(arr) - i - 1]
    print(sum1, sum2)
    return abs(sum1 - sum2)

print(diag_diff(arr))