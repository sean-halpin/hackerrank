package com.plusminus;
import java.util.List;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }

    /**
     * @param arr List of integers
     * @return void
     * @see https://www.hackerrank.com/challenges/plus-minus/problem
     * 
     *      Given an array of integers, calculate the fractions of its elements that
     *      are positive, negative, and are zeros.
     */
    public static double[] plusMinus(List<Integer> arr) {
        int n = arr.size();
        int pos = 0;
        int neg = 0;
        int zero = 0;
        for (int i = 0; i < n; i++) {
            if (arr.get(i) > 0) {
                pos++;
            } else if (arr.get(i) < 0) {
                neg++;
            } else {
                zero++;
            }
        }
        System.out.println((double) pos / n);
        System.out.println((double) neg / n);
        System.out.println((double) zero / n);
        return new double[] { (double) pos / n, (double) neg / n, (double) zero / n };
    }
}
