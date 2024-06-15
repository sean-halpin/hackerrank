# Recursion

- Recursion is a technique where a function makes one or more calls to itself. 
- It is a way to solve problems that have repeated computations. 
- Recursion is a common mathematical and programming concept. 
- It means that a function calls itself. 
- This has the benefit of meaning that you can loop through data to reach a result.

## Example

```python
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
```

```python
print(factorial(5)) # 120
```

## Recursive Data Structures

- Recursion is especially useful when working with recursive data structures. 
- A recursive data structure is a data structure that has a part that is similar to the whole. 
- One of the most common examples of a recursive data structure is the linked list. 
- A linked list is a list that has a node that points to another node. 
- This is a recursive data structure because the node structure is used in the definition of the whole linked list.

## The Call Stack

- A call stack is a stack data structure that stores information about the active subroutines of a computer program. 
- When a program calls a function, the function goes onto the call stack. 
- When a function returns, the function comes off the call stack. 
- The call stack uses a last-in, first-out (LIFO) data structure to store information about the active subroutines of a program. 
- When a program calls a function, the function goes onto the call stack. 
- When a function returns, the function comes off the call stack. 
- The call stack uses a last-in, first-out (LIFO) data structure to store information about the active subroutines of a program.
```

# Recursive Data Structures
- A recursive data structure is a data structure that has a part that is similar to the whole. 
- One of the most common examples of a recursive data structure is the linked list. 
- A linked list is a list that has a node that points to another node. 
- This is a recursive data structure because the node structure is used in the definition of the whole linked list.

# The Call Stack
- A call stack is a stack data structure that stores information about the active subroutines of a computer program. 
- When a program calls a function, the