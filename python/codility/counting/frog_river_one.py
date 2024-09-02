# X = 5
# A = [1,3,7,9,4,2,5,3,1]
# idx [0,1,2,3,4,5,6,7,8]

# create a set with all required positions to fill
# pathSet = set([1,2,3,4,5])

# We will loop through A, removing each element in A from pathSet until len(path) is zero. 
# Loop through A is O(N) 
# Check if element is in set is - best case O(1) and worst case O(n), in case of hash collisions
# and remove from set is same as checking if an element is in the set

def solution(X, A):
    pathSet = set(range(1,X+1))
    for i,n in enumerate(A): 
        if n in pathSet:
            pathSet.remove(n)
            if len(pathSet) == 0:
                return i
    return -1