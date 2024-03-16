# Array or List

| Index | Fruit Type |
|-------|------------|
|   0   | Apple      |
|   1   | Orange     |
|   2   | Banana     |
|   3   | Melon      |
|   4   | Kiwi       |

| Operation          | Big-O Complexity |
|--------------------|-----------------|
| Lookup             | O(1)            |
| Push               | O(1)            |
| Insert             | O(n)            |
| Delete             | O(n)            |

# Static vs Dynamic Arrays

Static are fixed size, Dynamic may grow on demand.

### Dynamic Array

| Operation          | Big-O Complexity |
|--------------------|-----------------|
| Lookup             | O(1)            |
| Append             | O(1)            |
| Insert             | O(n)            |
| Delete             | O(n)            |

# Reverse a string with Java

```
public class ReverseString {
    public static void main(String[] args) {
        String str = "Hello, World!";
        String reversed = reverseString(str);
        System.out.println(reversed);
    }

    public static String reverseString(String str) {
        char[] charArray = str.toCharArray();
        int left = 0;
        int right = charArray.length - 1;

        while (left < right) {
            char temp = charArray[left];
            charArray[left] = charArray[right];
            charArray[right] = temp;
            left++;
            right--;
        }

        return new String(charArray);
    }
}
```

# Merge Sorted integer arrays

```
public class MergeSortedArrays {
    public static void main(String[] args) {
        int[] arr1 = {1, 3, 5};
        int[] arr2 = {2, 4, 6};
        int[] merged = mergeArrays(arr1, arr2);
        System.out.println(Arrays.toString(merged));
    }

    public static int[] mergeArrays(int[] arr1, int[] arr2) {
        int[] merged = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0;

        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                merged[k++] = arr1[i++];
            } else {
                merged[k++] = arr2[j++];
            }
        }

        while (i < arr1.length) {
            merged[k++] = arr1[i++];
        }

        while (j < arr2.length) {
            merged[k++] = arr2[j++];
        }

        return merged;
    }
}

```
