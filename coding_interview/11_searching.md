# Search

## Linear Search

Process of searching a list sequentially for an item matching some criteria.
Best case O(1) - element is in first place you look
Worst case O(n) - element is in the last place you look

## Binary Search

If the array is sorted, we could use binary search. 
Start in the middle of the list & discard the half of the data which is no longer needed, then repeat. 
This would essentially be like a binary search tree. It requires sorting, but iteration is then much faster. 
Worst case O(log(n))

# Graph & Tree Traversals

Used a lot when we need to often search or traverse our data

## BFS

Breadth First Search (BFS) is a graph traversal algorithm that explores all the vertices of a graph in breadth-first order, i.e., it visits all the vertices at the same level before moving to the next level. 

The algorithm uses a queue data structure to keep track of the vertices to be visited. It starts by visiting the root node and enqueues its adjacent vertices. Then, it dequeues a vertex from the queue, visits its adjacent vertices, and enqueues them if they haven't been visited yet. This process continues until all the vertices have been visited or the queue becomes empty.

BFS is commonly used to find the shortest path between two vertices in an unweighted graph, as it guarantees that the shortest path will be found when all edges have the same weight.

The time complexity of BFS is O(V + E), where V is the number of vertices and E is the number of edges in the graph.

## DFS

Depth First Search (DFS) is a graph traversal algorithm that explores all the vertices of a graph by going as deep as possible before backtracking. It starts at a given vertex and explores as far as possible along each branch before backtracking.

Here's how DFS works:

Start at a given vertex (usually the root) and mark it as visited.
Explore one of its unvisited neighbors.
If there are unvisited neighbors, repeat step 2 for one of them.
If all neighbors have been visited, backtrack to the previous vertex and repeat step 2 for its unvisited neighbors.
Continue this process until all vertices have been visited.
DFS is commonly used to traverse or search through a graph or tree data structure. It can be used to find connected components, detect cycles, perform topological sorting, and more.

The time complexity of DFS is O(V + E), where V is the number of vertices and E is the number of edges in the graph.

## BFS vs DFS

Sure, here is a concise comparison of BFS (Breadth First Search) and DFS (Depth First Search):

#### BFS

Explores all vertices at the same level before moving to the next level.
Uses a queue data structure.
Guarantees finding the shortest path in an unweighted graph.
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.

#### DFS

Explores as deep as possible before backtracking.
Uses a stack data structure (or recursion).
Can be used for various tasks like finding connected components, detecting cycles, and performing topological sorting.
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
Both algorithms have the same time complexity, but they differ in their exploration strategy. BFS explores breadth-first, while DFS explores depth-first.
