# Recursion

A function that refers to itself. 

```java
public class StringReversal {
    public static String reverse(String str) {
        if (str.isEmpty()) {
            return str;
        }
        return reverse(str.substring(1)) + str.charAt(0);
    }
}
```
