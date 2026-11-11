# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next_node=None):
#         self.val = val
#         self.next_node = next_node

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        p, c = None, head
        
        while c:
            next_node = c.next
            c.next = p
            p = c
            c = next_node

        return p

        