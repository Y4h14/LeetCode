# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        curr, left_prev = head, dummy

        # find the left node
        for i in range(left -1):
            left_prev, curr = curr, curr.next

        # reverse between left and right
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # fix pointers
        left_prev.next.next = curr
        left_prev.next = prev
        return dummy.next