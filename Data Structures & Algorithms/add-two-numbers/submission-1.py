# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp = ans
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            curr = v1 + v2 + carry

            carry = curr // 10
            curr = curr % 10

            node = ListNode(curr)
            temp.next = node
            temp = node

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        if carry == 1:
            temp.next = ListNode(1)

        return ans.next