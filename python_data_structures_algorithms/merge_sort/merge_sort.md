# Merge Sort

Is a comparison based divide and conquer sorting algorithm

## Algorithm
1. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.

## Complexity
- Time complexity: O(n log n)
  - Because; the list is divided into log n parts and each part is merged in linear time
- Space complexity: O(n)

## References
- [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
- [GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)

## Implementations Python

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

arr = [12, 11, 13, 5, 6, 7]
print("Given array is", arr)
print("Sorted array is", merge_sort(arr))
```
The above code is a simple implementation of merge sort in python. The function merge_sort() takes an array as input and returns the sorted array. The function first divides the input array into two halves and then recursively sorts the two halves. Finally, the two sorted halves are merged to produce the final sorted array.
```
