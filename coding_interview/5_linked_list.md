# Linked List

A data structure consisting of nodes, where each node contains data and also a link to the next node. 

Additionally the head & tail references are kept for use in Linked List operations such as insert/add.

LL must be traversed to find items. This makes item iteration slower than Arrays for example.

```
public class LinkedList<T> {
    private Node<T> head;
    private Node<T> tail;

    private static class Node<T> {
        T data;
        Node<T> next;

        public Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    public void add(T data) {
        Node<T> newNode = new Node<>(data);

        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
    }

    // Other methods such as remove, search, etc. can be added here

    // Example method to print the linked list
    public void printList() {
        Node<T> current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
}
```

LinkedList are commonly used over Arrays where the order of data may be important, LinkedList can offer performance gains in this way, where the data is commonly manipulated.

LL can have sorted data since there is a notion of order. 

# Doubly Linked List

Similat to a Linked List, except that each node also contains a pointer to the previous node. 

Allows use to traverse in reverse. 

# Single vs Double LL

Single;

Less memory. Less Ops. Cannot be traversed in reverse.

Double; 

Better Search Perf. More Complex. More ops. 