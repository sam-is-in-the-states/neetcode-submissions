class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-val, idx) for idx, val in enumerate(nums[:k-1])]
        heapq.heapify(q)
        ans = []
        for i in range(k-1, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] < i-k+1:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans