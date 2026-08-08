# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        m = {}

        def helper(root, can_rob):
            if root is None:
                return 0
            
            if (root, can_rob) in m:
                return m[(root, can_rob)]
            
            ans = 0
            if not can_rob:
                ans += helper(root.left, True)
                ans += helper(root.right, True)
            
            else:
                ans1 = 0
                ans2 = root.val
                ans1 += helper(root.left, True)
                ans1 += helper(root.right, True)
                ans2 += helper(root.left, False)
                ans2 += helper(root.right, False)
                ans = max(ans1, ans2)
            m[(root, can_rob)] = ans
            return ans
        
        return helper(root, True)
