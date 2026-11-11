# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2, h = head1, head2, None
        if c1 and c2:
            if c1.val < c2.val:
                h = c1
                c1 = c1.next
            else:
                h = c2
                c2 = c2.next
        elif c1:
            return c1
        elif c2:
            return c2
        
        c = h
        
        while c1 and c2:
            if c1.val < c2.val:
                c.next = c1
                c1 = c1.next
            else:
                c.next = c2
                c2 = c2.next
            c = c.next

        if c1:
            c.next= c1
        if c2:
            c.next = c2
        return h	


        