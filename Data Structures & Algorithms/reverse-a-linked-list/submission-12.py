# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next_node=None):
#         self.val = val
#         self.next_node = next_node

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        prev_node = None
        curr_node = head
        
        while curr_node:
            next_node = curr_node.next_node
            curr_node.next_node = prev_node
            prev_nodec= curr_node
            curr_node = next_node
            
        return prev

        