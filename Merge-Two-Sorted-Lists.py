# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        head = res
        
        if not list1:
            return list2
        if not list2:
            return list1
    
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val > p2.val:
                res.next = p2
                res =res.next
                p2 = p2.next
            else:
                res.next = p1
                res = res.next
                p1 = p1.next
        res.next = p1 if p1 else p2

        return head.next