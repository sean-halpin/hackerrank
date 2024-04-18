# Sorting

## Bubble Sort

Explanation: Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
 - Pros: Simple implementation, works well for small datasets.
 - Cons: Inefficient for large datasets, has a time complexity of O(n^2).

## Selection Sort

Explanation: Selection Sort divides the input into a sorted and an unsorted region, repeatedly selects the smallest element from the unsorted region and places it in the sorted region.
 - Pros: Simple implementation, performs well for small datasets.
 - Cons: Inefficient for large datasets, has a time complexity of O(n^2).

## Insertion Sort

Explanation: Insertion Sort builds the final sorted array one item at a time, by repeatedly inserting a selected element into the correct position.
 - Pros: Efficient for small datasets and partially sorted arrays, stable sorting algorithm.
 - Cons: Inefficient for large datasets, has a time complexity of O(n^2).

## Merge Sort

Explanation: Merge Sort divides the input into smaller subarrays, recursively sorts them, and then merges them to obtain a sorted array.
 - Pros: Efficient for large datasets, has a time complexity of O(n log n), stable sorting algorithm.
 - Cons: Requires additional memory for the merging process.

## Quick Sort

Explanation: Quick Sort selects a pivot element, partitions the array around the pivot, and recursively sorts the subarrays.
 - Pros: Efficient for large datasets, has an average time complexity of O(n log n), in-place sorting algorithm.
 - Cons: Worst-case time complexity of O(n^2) if the pivot selection is poor.

## Radix Sort

Explanation: Radix Sort sorts the elements by processing individual digits or groups of digits, from the least significant to the most significant.
 - Pros: Efficient for sorting integers with a fixed number of digits, has a time complexity of O(k * n), where k is the number of digits.
 - Cons: Limited to sorting integers, requires additional memory.

## Heap Sort

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements. It works by building a max heap or min heap from the input array and repeatedly extracting the root element to obtain a sorted array.

Pros
 - Efficient for large datasets.
 - Guaranteed worst-case time complexity of O(n log n).
 - In-place sorting algorithm, meaning it doesn't require additional memory.

Cons of Heap Sort:  
 - Not stable, meaning it may change the relative order of equal elements.
 - Requires knowledge of heap data structure.
 - Slower than some other sorting algorithms for small datasets.


### Quick Sort Implementation

```java
public class QuickSort {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 7, 6, 3};
        quickSort(arr, 0, arr.length - 1);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }
}
```

### Merge Sort

```java
public class MergeSort {
    public static void mergeSort(int[] arr, int low, int high) {
        if (low < high) {
            int mid = (low + high) / 2;
            mergeSort(arr, low, mid);
            mergeSort(arr, mid + 1, high);
            merge(arr, low, mid, high);
        }
    }

    private static void merge(int[] arr, int low, int mid, int high) {
        int[] temp = new int[high - low + 1];
        int i = low;
        int j = mid + 1;
        int k = 0;

        while (i <= mid && j <= high) {
            if (arr[i] <= arr[j]) {
                temp[k] = arr[i];
                i++;
            } else {
                temp[k] = arr[j];
                j++;
            }
            k++;
        }

        while (i <= mid) {
            temp[k] = arr[i];
            i++;
            k++;
        }

        while (j <= high) {
            temp[k] = arr[j];
            j++;
            k++;
        }

        for (int x = 0; x < temp.length; x++) {
            arr[low + x] = temp[x];
        }
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 7, 6, 3};
        mergeSort(arr, 0, arr.length - 1);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }
}
```