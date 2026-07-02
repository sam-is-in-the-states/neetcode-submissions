# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(root, cur_max):
            if not root:
                return 0
            ans = 0
            if root.val >= cur_max:
                ans = 1
                cur_max = root.val
            
            return ans + helper(root.left, cur_max) + helper(root.right, cur_max)
        
        return helper(root, float('-inf'))
