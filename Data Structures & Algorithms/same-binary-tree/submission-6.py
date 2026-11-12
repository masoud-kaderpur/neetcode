# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs
        # if not p and not q:
        #     return True
        # if p and q and p.val == q.val:            
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
        # else:
        #     return False
        # bfs
        if not p and not q:
            return True
        q = deque([p,q])
        
        while q:
            nodep, nodeq = q.popleft()
            if not nodep and not nodeq:
                continue
            if nodep and nodeq and nodep.val != nodeq.val:
                return False
            q.append(nodep.left, nodeq.left)
            q.append(nodep.right, nodeq.right)
            
            

        