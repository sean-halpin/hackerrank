# Stack 

A LIFO data structure

- **Last In First Out**
- **Push** adds to the top
- **Pop** removes from the top
- **Peek** looks at the top item
- **isEmpty** checks if the stack is empty

### Stack Class

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

# Usage
s = Stack()
s.push(1)
s.push('two')
print(s.peek()) # 'two'
print(s.pop()) # 'two'
print(s.isEmpty()) # False
print(s.pop()) # 1
print(s.isEmpty()) # True
```

### Stack with a List

```python
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack) # [1, 2, 3]

print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
```

### Stack with a Deque

```python
from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack) # deque([1, 2, 3])

print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
```

### Stack with a List

```python
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack) # [1, 2, 3]

print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
```

### Stack with a Deque

```python
from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack) # deque([1, 2, 3])

print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
```