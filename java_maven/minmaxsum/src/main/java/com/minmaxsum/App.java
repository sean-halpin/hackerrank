package com.minmaxsum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        ArrayList<Integer> arr = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));
        miniMaxSum(arr);
    }

    public static void miniMaxSum(List<Integer> arr) {
        Collections.sort(arr);
        Long smallSum = 0L;
        Long bigSum = 0L;
        for(Integer i = 0; i < arr.size() - 1; i++){
            smallSum += arr.get(i);
        }
        for(Integer i = 1; i < arr.size(); i++){
            bigSum += arr.get(i);
        }
        System.out.println(smallSum + " " + bigSum);
    }
}
