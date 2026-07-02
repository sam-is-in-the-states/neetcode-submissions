# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        curr = []
        from collections import deque
        q = deque()
        q.append(root)
        qlen = 1
        while q:
            for _ in range(qlen):
                elt = q.popleft()
                if not elt:
                    continue
                q.append(elt.left)
                q.append(elt.right)
                curr.append(elt.val)
            if curr:
                ans.append(curr[-1])
            curr = []
            qlen = len(q)
        return ans
