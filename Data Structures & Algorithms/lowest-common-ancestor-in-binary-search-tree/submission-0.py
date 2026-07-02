# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p,q = q,p
        
        def helper(r):
            if r.val == p.val or r.val == q.val:
                return r
            if p.val < r.val < q.val:
                return r
            if r.val < p.val:
                return helper(r.right)
            
            return helper(r.left)
        
        return helper(root)