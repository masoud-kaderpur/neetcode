# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        q = deque()
        c = head	

        while c:
            q.append(c)
            c = c.next

        c = q.popleft()
        i = 1

        while q:
            if i % 2 == 1:
                c.next = q.pop()
            else:
                c.next = q.popleft()
            i += 1
            c = c.next
        
        c.next = None

        