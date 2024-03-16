# HashMap

```
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        // Create and initialize a HashMap
        HashMap<String, Integer> hashMap = new HashMap<>();
        hashMap.put("apple", 1);
        hashMap.put("banana", 2);
        hashMap.put("orange", 3);

        // Accessing elements
        int value = hashMap.get("apple");
        System.out.println("Value of 'apple': " + value);

        // Checking if a key exists
        boolean containsKey = hashMap.containsKey("banana");
        System.out.println("Contains key 'banana': " + containsKey);

        // Checking if a value exists
        boolean containsValue = hashMap.containsValue(3);
        System.out.println("Contains value '3': " + containsValue);

        // Removing an element
        hashMap.remove("orange");
        System.out.println("HashMap after removing 'orange': " + hashMap);

        // Size of the HashMap
        int size = hashMap.size();
        System.out.println("Size of the HashMap: " + size);

        // Clearing the HashMap
        hashMap.clear();
        System.out.println("HashMap after clearing: " + hashMap);
    }
}

```

# Hash Function

Func that generates an output of fixed length given any length input. 
Examples; MD5(fast), SHA256(slow)

Hash Functions should be 1 way, given a hash it should not be possible to discover the exact input. 
It should also be idempotent, meaning the output should be identical and repeatable for a given input.

Hash Functions are used to decide the index/address of an element in a HashMap for a given key.

insert/lookup/delete/search should all be O(1), because the hash function tells us exactly where to find an item in memory given the key. 

# Hash Collisions

When multiple keys arrive at the same hash, this is a collision. 

# Collision Resolution

One solution for this, is that the hash table implementation keeps a linked list, and keys that collide are stored in a linkedlist at the same address. 

This has a downside in that the worst case, we could have O(n) for hash table operations. 