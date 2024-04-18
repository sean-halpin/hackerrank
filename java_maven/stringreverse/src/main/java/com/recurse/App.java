package com.recurse;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        System.out.println(reverse("Hello World!"));
    }

    public static String reverse(String str) {
        if (str.isEmpty() || str == null) {
            return str;
        } else {
            return reverse(str.substring(1)) + str.charAt(0);
        }
    }
}
