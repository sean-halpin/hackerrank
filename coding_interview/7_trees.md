# Trees

Trees have a hierarchical structure. 
 - Each tree begins with a single root node, 
 - each node can have multiple child nodes, 
 - child nodes have a parent, 
 - child nodes without child nodes are leaves, 
 - node of the same level are siblings

## Examples

 - html and xml are tree like structures. 
 - LinkedList is a tree, with a single path & single child and parent per node.

# Binary Search Trees

Binary trees are a type of tree data structure where each node can have at most two child nodes.
The left child is smaller than the parent node, while the right child is greater. 

 - This property makes binary trees useful for efficient searching and sorting operations. 
 - Each node in a binary tree can have zero, one, or two child nodes, and nodes without any children are called leaf nodes. 
 - Binary trees are commonly used in various algorithms and data structures, such as binary search trees and heaps.

### Perfect Binary Tree

A perfect binary tree is a type of binary tree where every level is fully filled, meaning each node has either two children or none. 
It's interesting because it's always balanced, ensuring operations like insertion, deletion, and lookup can be performed in logarithmic time (O(log n)).
 Additionally, it has the maximum number of nodes possible for a binary tree of its height, which is 2^h - 1. However, perfect binary trees are rare in practical applications due to their precise requirements.

BST most ops are better than O(n)
BST are ordered
BST are dynamic/flexible size
However, there are no O(1) operations

### AVL Tree , Red Black Tree

Auto Balancing Trees

## Binary Heaps

### Max Heap

A max heap is a specialized tree-based data structure that satisfies the heap property. 
 - In a max heap, for any given node I, the value of I is greater than or equal to the values of its children. 
 - This property ensures that the maximum element of the heap is always at the root node. 
 - Max heaps are commonly used in implementations of priority queues and heap sort algorithms.

```
              100
            /      \
          19        36
         /  \      /  \
        17   3    25   1
       / \  / \   / \
      2  7  9  8  5  4
```

Note: Memory Heap is not related to Heap Data Structure. 

## Priority Queue

Can implement the max priority queue using a max heap

## Trie / Prefix Tree

```
                root
               /   \
              a     b
             / \   / \
            n   p o   y
```

A Trie, also known as a Prefix Tree, is a tree-like data structure that is used to store a collection of strings. 
 - Each node of the Trie represents a single character and each path from the root to a leaf node represents a word from the collection.

Tries are mainly used for efficient retrieval of words in a language, providing autocomplete suggestions, and implementing spell checkers. 
 - Their advantage is that they allow for fast lookups, insertions, and deletions, often in O(n) time, where k is the length of the key (string).