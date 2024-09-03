from functools import reduce

# This solution does not account for 2 smallest negative numbers possibly having the biggest product
def solution(A):
    A.sort()
    # [1,2,3,4]
    largest = A[len(A)-3:]
    return reduce(lambda x,y: x*y, largest)

def solution_incl_neg(A):
    # Implement your solution here
    A.sort()
    # [1,2,3,4]
    largest = A[-1] * A[-2] * A[-3]
    largest_neg = A[0] * A[1] * A[-1]
    return max(largest, largest_neg)

