# Url: https://leetcode.com/problems/sort-list/
# Tags: ['Linked List', 'Divide and Conquer', 'Sorting']

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort(A):
    L = len(A)
    if L <= 1:
        return A
    midpoint = L // 2
    left = A[:midpoint]
    right = A[midpoint:]
    l_merge = merge_sort(left)
    r_merge = merge_sort(right)
    return merge(l_merge,r_merge)

def merge(A, B):
    L = len(A)
    R = len(B)
    i = 0
    j = 0
    result = []
    while i < L and j < R:
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        elif A[i] >= B[j]:
            result.append(B[j])
            j += 1
    if i >= L:
        result = result + B[j:]
    elif j >= R:
        result = result + A[i:]
    return result

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        unsorted = []
        while head:
            unsorted.append(head.val)
            head = head.next

        sortedVals = merge_sort(unsorted)
        new_head = ListNode(sortedVals[0], None)
        curr = new_head
        for i in range(1, len(sortedVals)):
            curr.next = ListNode(sortedVals[i], None)
            curr = curr.next
        return new_head
    