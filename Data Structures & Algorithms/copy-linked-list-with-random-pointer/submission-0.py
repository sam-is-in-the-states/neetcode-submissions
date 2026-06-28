"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        temp = head

        while temp:
            new = Node(temp.val, next = temp.next)
            nxt = temp.next
            temp.next = new
            temp = nxt
        
        temp = head

        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next

        temp = head
        ans = head.next


        while temp:
            temp1 = temp.next
            temp.next = temp.next.next
            temp = temp.next
            temp1.next = temp1.next.next if temp1.next else None
        
        return ans
            