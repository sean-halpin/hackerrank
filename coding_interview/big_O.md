# Big O Notation

[Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

Big-O Notation allows us to measure the time or space complexity of algorithms.
It is useful for measuring and comparing code to determine which is most scalable. 

Big-O indicates the worst case performance given the size of the input. 
It is the relationship between the ops or space needed given the number of inputs. 

# Linear O(n)

```java
for (int i = 0; i < n; i++) {
    // Big O of for loop is linear, O(n)
}
```

# Constant O(1)

```java
public static void main(String[] args) {
    if (args.length > 0) {
        System.out.println(args[0]); // Big-O is constant, 
        // no matter the size of input, the numbers of ops is constant.
    }
}
```

# Evaluate 
```java
int n = 10; // O(1)
int m = 10; // O(1)
for (int i = 0; i < n; i++) {
    // Big O of for loop is linear, O(n)
}
for (int i = 0; i < m; i++) {
    // Big O of for loop is linear, O(n)
}
for (int i = 0; i < n/2; i++) {
    // Big O of for loop is linear, O(n/2)
}
for (int i = 0; i < 100; i++) {
    // Big O of for loop is linear, O(100)
}
```
O(n + n + n/2 + 100)
Solution: O(n)

```java
public void loopOverLists(List<Integer> list1, List<Integer> list2) {
    for (int i = 0; i < list1.size(); i++) {
        // code inside the loop
    }
    for (int i = 0; i < list2.size(); i++) {
        // code inside the loop
    }
}
```
Solution: O(a+b) or O(n+m) for example (Rule 3)

# O(n^2) Quadratic

```java
public void printElements(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < arr.length; j++) {
            System.out.println("Element i: " + arr[i] + ", Element j: " + arr[j]);
        }
    }
}
```

# O(n!) Factorial

Very bad - a loop for each element for example. 

# Rules - Resolving Big-O

1. Look at the worst case flow. 
2. Drop Constants
3. Different Terms for inputs
4. Drop non dominants

# What causes space complexity

1. Variables
2. Data Structures
3. Function Calls - Stack Frames
4. Allocations