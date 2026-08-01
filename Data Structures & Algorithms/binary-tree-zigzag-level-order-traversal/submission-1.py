# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque()
        q.append(root)
        ans = []
        curr = []
        alt = True
        while q:
            n = len(q)
            for _ in range(n):
                elt = q.popleft()
                if not elt:
                    continue
                curr.append(elt.val)
                q.append(elt.left)
                q.append(elt.right)
            
            if curr:
                if alt:
                    ans.append(curr)
                    alt = False
                else:
                    ans.append(curr[::-1])
                    alt = True
                curr = []
        return ans

        