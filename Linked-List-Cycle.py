# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = ListNode()
        slow.next = head
        fast = head

        while fast and fast.next:
            if slow == fast:
                return True
            
            fast = (fast.next).next
            slow = slow.next
        
        return False
                