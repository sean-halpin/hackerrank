# Linked List

```
head
  |
  v
+----+    +----+    +----+    +----+    +----+
| 1  |--->| 2  |--->| 3  |--->| 4  |--->| 5  |
+----+    +----+    +----+    +----+    +----+
                                            ^
                                            |
                                            tail
```

## LL Operations

- Append()
  - O(1)
  - tail node points to new node
  - tail pointer updated to new node
- Pop()
  - O(n)
  - iterate list, find node pointing to tail node
  - point tail at n-1
  - point new tail node to none
- Insert(0,1)
  - O(1)
  - point new node to head node
  - point head to new node
- Insert(n,1)
  - O(n)
  - iterate list, find node n
  - point new node to node n + 1
  - point node n to new node
- Pop(n)
  - O(n)
  - iterate list, find element n
  - point element n-1 to n+1