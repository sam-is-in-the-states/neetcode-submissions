# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        ans = ListNode()
        ans.next = head

        temp = ans
        while left > 1:
            temp = temp.next
            left -= 1
            right -= 1
        
        l = temp
        temp = temp.next
        prev = temp
        temp = temp.next
        right -= 2

        while right > 0:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            right -= 1
        
        l.next.next = temp.next
        temp.next = prev
        l.next = temp
        return ans.next
            