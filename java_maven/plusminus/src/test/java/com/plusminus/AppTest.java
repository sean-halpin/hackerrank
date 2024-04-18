package com.plusminus;

import static org.junit.Assert.assertArrayEquals;

import java.util.Arrays;
import java.util.List;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

public class AppTest extends TestCase {

    public AppTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(AppTest.class);
    }

    public void testPlusMinus() {
        // Test case 1
        List<Integer> arr1 = Arrays.asList(1, -2, 3, -4, 0);
        double[] expected = new double[] { 0.4, 0.4, 0.2 };
        double[] actual = App.plusMinus(arr1);
        assertArrayEquals(expected, actual, 0.0000001);
        // Test case 2
        List<Integer> arr2 = Arrays.asList(1, 2, 3, 4, 5);
        expected = new double[] { 1.0, 0.0, 0.0 };
        actual = App.plusMinus(arr2);
        assertArrayEquals(expected, actual, 0.0000001);
        // Test case 3
        List<Integer> arr3 = Arrays.asList(-1, -2, -3, -4, -5);
        expected = new double[] { 0.0, 1.0, 0.0 };
        actual = App.plusMinus(arr3);
        assertArrayEquals(expected, actual, 0.0000001);
    }
}