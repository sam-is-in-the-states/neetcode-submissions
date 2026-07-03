class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heapify, heappush, heappop
        def get_dist(x,y):
            return math.sqrt(x*x + y*y)
        q = [(get_dist(*num), num) for num in points]
        heapify(q)

        ans = []
        for _ in range(k):
            ans.append(heappop(q)[1])
        
        return ans