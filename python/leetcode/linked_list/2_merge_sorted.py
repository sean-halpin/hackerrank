# leetcode url: https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        if not list1:
            tail.next = list2
        elif not list2:
            tail.next = list1

        return head.next
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = sol.mergeTwoLists(l1, l2)
    assert l3.val == 1
    assert l3.next.val == 1
    assert l3.next.next.val == 2
    assert l3.next.next.next.val == 3
    assert l3.next.next.next.next.val == 4
    assert l3.next.next.next.next.next.val == 4
    assert l3.next.next.next.next.next.next == None
    print("Example 1 is correct")
    
