# Bubble Sort: Repeatedly swap adjacent elements if they are in the wrong order, until the list is sorted.

def bubble_sort(arr):
    print(arr, "\n")
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

if __name__ == "__main__":
    unsorted = [6,2,9,3,4]
    result = bubble_sort(unsorted)
    print(result)
    assert result == [2,3,4,6,9]   