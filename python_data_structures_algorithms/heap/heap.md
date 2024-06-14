# Heap

A heap is an abstract data structure, a special type of tree called a complete tree. 
Where each level in the tree is filled from left to right befor moving to the next level. 

Heaps are often used in Priority Queues. A heap is different to a binary search tree in that it can have duplicates. 

- **Heap Property**: The key at the root is the minimum or maximum key in the tree. 

### Binary Heap

A binary heap is a complete binary tree. 

- **Min Heap**: The key at the root is the minimum key in the tree. 
- **Max Heap**: The key at the root is the maximum key in the tree. 

### Heap Operations

- **Insert**: Add an element to the heap
- **Extract**: Remove the minimum or maximum element
- **Heapify**: Convert an array into a heap

### Heap Class

```python
class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.heapify()

    def extract(self):
        return self.heap.pop(0)

    def heapify(self):
        n = len(self.heap)
        for i in range(n//2-1, -1, -1):
            self.heapifyUtil(i)

    def heapifyUtil(self, i):
        n = len(self.heap)
        left = 2*i + 1
        right = 2*i + 2
        smallest = i
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapifyUtil(smallest)

# Usage
h = Heap()
h.insert(3)
h.insert(2)
h.insert(1)
print(h.extract()) # 1
print(h.extract()) # 2
print(h.extract()) # 3
```

### Heap with a List

```python
heap = []

heap.append(3)
heap.append(2)
heap.append(1)

print(heap) # [3, 2, 1]

print(heap.pop(0)) # 3
print(heap.pop(0)) # 2
print(heap.pop(0)) # 1
```

### Heap with a Priority Queue

```python
from queue import PriorityQueue

q = PriorityQueue()

q.put(3)
q.put(2)
q.put(1)

print(q.get()) # 1
print(q.get()) # 2
print(q.get()) # 3