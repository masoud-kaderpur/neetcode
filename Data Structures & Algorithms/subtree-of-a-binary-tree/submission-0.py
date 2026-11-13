# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q1 = deque([root])
        q2 = deque([subRoot])
        while q1 and q2:
            c1 = q1.popleft()
            if c1 == q2[0]:
                c2 = q2.popleft()
                if c2.left:
                    q2.append(c2.left)
                if c2.right:
                    q2.append(c2.right)		
            if c1.left:
                q1.append(c1.left)
            if c1.right:
                q1.append(c1.right)
            
        if q2:
            return False
        else:
            return True