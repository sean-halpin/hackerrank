arr = [1,1,3,2,1]

def counting_sort(arr):
    freqArray = [0] * 100
    for i in arr: 
        freqArray[i] += 1
    print(freqArray)
    # sortedArray = [] 
    # for i in range(len(freqArray)):
    #     if freqArray[i] != 0:
    #         sortedArray.extend([i] * freqArray[i])
    # return sortedArray
    return freqArray

print(counting_sort(arr))