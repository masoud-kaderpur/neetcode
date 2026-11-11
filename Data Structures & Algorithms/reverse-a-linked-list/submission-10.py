# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p = None
        c = head
        n = c.next
        while c is not None:
            c.next = p
            p = c
            c = n
            if c is not None:
                n = c.next
        return p

        