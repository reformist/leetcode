# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# need to detect a linkedlist cycle

# it's like a tortoise and hare problem. need to see if tortoise ever goes ahead of the hare. the way to do this to 
# set two pointers on the head and then iterate them with slow moving one at a time and fast moving two at a time
# while loop for fast and fast.next to make sure aren't iterating on null values
# when they're equal there's a loop. then break out

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Check if the linked list is empty or has only one node
        fast = slow = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        
        return False

        
        
        
