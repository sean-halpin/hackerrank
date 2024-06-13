# Trees

A tree is an abstract data type. 

- A tree is a collection of nodes. 
- Each node has a value and a list of references to other nodes. 
- The nodes are connected by edges. 
- The top node is called the root. 
- Nodes with no children are called leaves. 
- Nodes with the same parent are called siblings. 
- The depth of a node is the length of the path to the root. 
- The height of a node is the longest path to a leaf. 


### Binary Trees

A binary tree is a tree in which each node has at most two children. 

- A binary tree is either empty or has:
  - A key
  - A left subtree
  - A right subtree

### Special Trees

- A Full tree is a tree in which each node has zero or two children. 
- A Perfect tree is a tree in which each level is full. 
- A Complete tree is a tree in which each level is full except for the last level. 
- A Balanced tree is a tree in which the left and right subtrees have similar heights. 

### Binary Search Trees

A binary search tree is a binary tree in which each node has a key. 

- The key in the left subtree is less than the key in the parent node. 
- The key in the right subtree is greater than the key in the parent node. 

### Tree Traversal

Tree traversal is the process of visiting each node in the tree exactly once. 

- **In-order**: Left, root, right
- **Pre-order**: Root, left, right
- **Post-order**: Left, right, root

### Binary Tree Class

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def contains(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.contains(root.right, key)
        return self.contains(root.left, key)

# Usage
tree = BinaryTree()
tree.root = tree.insert(None, 1)
tree.insert(tree.root, 2)
tree.insert(tree.root, 3)
tree.insert(tree.root, 4)
tree.insert(tree.root, 5)

print("Inorder")
tree.inorder(tree.root)

print("Preorder")
tree.preorder(tree.root)

print("Postorder")
tree.postorder(tree.root)
```

### Binary Search Tree Class

```python
class Node: