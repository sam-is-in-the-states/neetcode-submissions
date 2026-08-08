# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        ans = TreeNode(target+1, root, None)

        def helper(root, prev, is_left):
            
            if root.left is not None:
                helper(root.left, root, True)
            
            if root.right is not None:
                helper(root.right, root, False)

            if root.left is None and root.right is None and root.val == target:
                if prev != None:
                    if is_left:
                        prev.left = None
                    else:
                        prev.right = None
        helper(ans.left, ans, True)
        return ans.left

            