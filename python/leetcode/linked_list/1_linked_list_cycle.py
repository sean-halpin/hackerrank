# Definition for singly-linked list.
from typing import Optional
# leetcode url: https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        # Initialize two pointers
        slow = head
        fast = head.next

        while slow != fast:
            # If fast pointer reaches the end, there's no cycle
            if not fast or not fast.next:
                return False
            
            # Move slow pointer one step, fast pointer two steps
            slow = slow.next
            fast = fast.next.next
        
        # If the loop exits, slow == fast, meaning there's a cycle
        return True
    
# Algorithm used: Floyd's Tortoise and Hare
# Time complexity: O(n)
# Space complexity: O(1)

# Approach:
# Initialize two pointers, slow and fast, at the head of the linked list.
# Move slow one step and fast two steps.
# If there's a cycle, slow and fast will meet at some point.
# If there's no cycle, fast will reach the end of the linked list.
# Return False in this case.
# Return True if slow and fast meet.

if __name__ == "__main__":
    # Example 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    assert Solution().hasCycle(head) == True
    

    # Example 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert Solution().hasCycle(head) == True

    # Example 3
    head = ListNode(1)
    assert Solution().hasCycle(head) == False