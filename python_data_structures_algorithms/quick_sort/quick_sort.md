# Quick Sort

Quicksort is a divide-and-conquer sorting algorithm.

## Algorithm
1. Choose a pivot element from the array. You can choose the first element, last element, middle element, or a random element as the pivot.
2. Partitioning: Rearrange the array in such a way that all elements less than the pivot are to the left of the pivot, and all elements greater than the pivot are to the right of the pivot.
3. Recursively apply the above steps to the sub-arrays to the left and right of the pivot.

## Complexity
- Time complexity: O(n log n) average case, O(n^2) worst case
  - Because; the list is divided into log n parts and each part is sorted in linear time
- Space complexity: O(log n)

## References
- [Wikipedia](https://en.wikipedia.org/wiki/Quicksort)
- [GeeksforGeeks](https://www.geeksforgeeks.org/quick-sort/)

## Implementations Python

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [12, 11, 13, 5, 6, 7]
print("Given array is", arr)
print("Sorted array is", quick_sort(arr))
```

The above code is a simple implementation of quick sort in python. The function quick_sort() takes an array as input and returns the sorted array. The function first chooses a pivot element from the array and then rearranges the array such that all elements less than the pivot are to the left of the pivot, and all elements greater than the pivot are to the right of the pivot. The function then recursively applies the above steps to the sub-arrays to the left and right of the pivot. Finally, the sorted sub-arrays are concatenated to produce the final sorted array.