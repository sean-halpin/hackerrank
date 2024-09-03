# The solution is based on the following observations:
# 1. For each disc, we can calculate the left and right boundaries of the disc.
# 2. We can sort the left and right boundaries of the discs.
# 3. We can iterate through the left boundaries and right boundaries of the discs and count the number of intersections.
# 4. We can keep track of the number of active discs at each point in time.
# 5. We can return the number of intersections.
#
# The time complexity of this solution is O(N*log(N)) due to the sorting operation.
# The space complexity of this solution is O(N) due to the left and right arrays.

def solution(A):
    l = len(A)
    left = [0] * l
    right = [0] * l

    for i in range(l):
        left[i] = i - A[i]
        right[i]= i + A[i]

    left.sort()
    right.sort()

    lidx = 0
    ridx = 0
    active_discs = 0
    intxs = 0

    while lidx < l:
        # print(lidx, l, len(left), len(right))
        if left[lidx] <= right[ridx]:
            intxs += active_discs
            active_discs += 1
            lidx += 1
        else:
            active_discs -= 1
            ridx += 1
        
        if intxs > 1_000_000_000:
            return -1

    return intxs