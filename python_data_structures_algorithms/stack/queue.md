# Queue

A FIFO linear data structure. 

- **First In First Out**
- **Enqueue** adds to the end
- **Dequeue** removes from the front
- **Peek** looks at the front item
- **isEmpty** checks if the queue is empty

### Queue Class

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()

    def peek(self):
        if self.queue:
            return self.queue[0]

    def isEmpty(self):
        return self.queue == []
```

### Queue with a List

```python
queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print(queue) # [1, 2, 3]

print(queue.pop(0)) # 1
print(queue.pop(0)) # 2
print(queue.pop(0)) # 3
```

### Queue with a Deque

```python
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue) # deque([1, 2, 3])

print(queue.popleft()) # 1
print(queue.popleft()) # 2
print(queue.popleft()) # 3
```
[]: # Links
[]: # [Python Data Structures & Algorithms + LEETCODE Exercises
[]: # ](https://www.udemy.com/course/data-structures-algorithms-python/learn/lecture/35369594#overview)
[]: # [Python Data Structures and algorithms](

