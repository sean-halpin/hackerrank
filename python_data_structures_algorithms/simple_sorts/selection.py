# Selection Sort: Repeatedly find the minimum element and move it to the sorted portion of the list.

def selection_sort(arr):
    print(arr, "\n")
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    unsorted = [6,2,9,3,4]
    result = selection_sort(unsorted)
    print(result)
    assert result == [2,3,4,6,9]   