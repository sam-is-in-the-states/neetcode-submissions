class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        counts = Counter(nums)
        q = [(-v,k) for k,v in counts.items()]
        heapq.heapify(q)
        ans = []
        for _ in range(k):
            elt = heapq.heappop(q)
            ans.append(elt[1])
        return ans
