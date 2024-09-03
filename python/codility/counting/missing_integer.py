def solution(A):
    mx = max(A)
    seen = set()
    if mx<=0:
        return 1
    for n in A:
        if n>0 and n not in seen:
            seen.add(n)
    for i in range(1,mx):
        if i not in seen:
            return i
    return mx + 1

# Write a function:

# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].