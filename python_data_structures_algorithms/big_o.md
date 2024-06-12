# Python Data Structures and algorithms

Notes for the Udemy Course: [Python Data Structures & Algorithms + LEETCODE Exercises
](https://www.udemy.com/course/data-structures-algorithms-python/learn/lecture/35369594#overview). 


## Big O

Measurement of time or space complexity for code. 

- Useful to compare code for time or space cost. 
  - How can we run it with lower time complexity?
  - What if space complexity is the priority?


## Notation

- Notation Letters
  - Omega, Best Case
  - Theta, Average Case
  - O, Worst Case
- Big O, is usually talking about worst case. 

## Common Time Complexities

- Constant Time
  - O(1)
    - Operations are constant and unrelated to input n
    - Most efficient
- Logarithmic Time
  - O(log n), very efficient with large number of n
  - Divide and Conquer
- Linear Time
  - O(n), linear relation between time and operations
- LogLinear Time
  - O(n log n)
  - Nearly as bad as quadratic time
  - Most efficient sorting algo time (except just numbers)
    - Merge Sort 
    - Quick Sort
- Quadratic Time
  - O(n^2), quadratic relation of time and ops


## Simplifiy Rules 

  Simplify Big O Calculation Rules
  - Drop Constants
    - O(2n) becomes O(n)
  - Drop Non Dominants
    - O(n^2 + n) becomes O(n^2)
      - As n grows the O(n) will become much less significant (non dominant)
  - Different terms for multiple inputs
    - O(a+b) != O(n)
    - O(a*b) != O(n^2)
