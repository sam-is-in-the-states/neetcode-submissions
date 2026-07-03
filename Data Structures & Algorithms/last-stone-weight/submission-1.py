from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        q = [-x for x in stones]
        heapq.heapify(q)
        while len(q) > 1:
            stone1 = -heapq.heappop(q)
            stone2 = -heapq.heappop(q)

            if stone1 == stone2:
                continue

            heapq.heappush(q, stone2-stone1)
        
        return -q[0] if q else 0
            
