# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heapify, heappush, heappop

        heap = [(l.val, idx, l) for idx, l in enumerate(lists) if l is not None]
        head = ListNode()
        temp = head

        heapify(heap)
        while heap:
            _, idx, node = heappop(heap)
            nxt = node.next
            node.next = None
            if nxt:
                heappush(heap, (nxt.val, idx, nxt))
            temp.next = node
            temp = node
        
        return head.next


