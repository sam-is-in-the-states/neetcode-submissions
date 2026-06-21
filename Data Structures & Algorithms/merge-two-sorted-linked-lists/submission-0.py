# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list2.val < list1.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        head.next = None
        ans = head
        while list1 and list2:
            if list2.val < list1.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
            head.next = None
        
        if not list1:
            head.next = list2
        else:
            head.next = list1
        return ans
        