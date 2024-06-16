# Insertion Sort: Repeatedly insert the next element into its correct position in the sorted portion of the list.

def insertion_sort(arr):
    print(arr, "\n")
    for i in range(1, len(arr)):
        j=i
        while j>0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr

if __name__ == "__main__":
    unsorted = [6,2,9,3,4]
    result = insertion_sort(unsorted)
    print(result)
    assert result == [2,3,4,6,9]   