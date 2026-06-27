# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ans = head

        temp = head
        slow = head

        while temp and temp.next:
            temp = temp.next.next
            slow = slow.next
        
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return head
            
            temp = head.next
            head.next = None
            while temp:
                curr = temp
                temp = temp.next
                curr.next = head
                head = curr
            # curr.next = None
            return head
        
        slow = reverseList(slow)

        temp = ans
        head = head.next
        while head and slow:
            temp.next = slow 
            slow = slow.next
            temp = temp.next

            temp.next = head 
            head = head.next
            temp = temp.next
        
        if head:
            temp.next = head 
            head.next = None
        
        if slow:
            temp.next = slow 
            slow.next = None
        
        
