class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 1
        min_q = [(nums[0], 0)]
        max_q = [(-nums[0], 0)]
        n = len(nums)
        max_idx = 0

        for i in range(1, n):
            heapq.heappush(min_q, (nums[i], i))
            heapq.heappush(max_q, (-nums[i], i))

            while max_q[0][1] < max_idx or min_q[0][1] < max_idx or -max_q[0][0] - min_q[0][0] > limit:
                if max_q[0][1] < max_idx:
                    heapq.heappop(max_q)
                    continue

                if min_q[0][1] < max_idx:
                    heapq.heappop(min_q)
                    continue
                
                if min_q[0][1] == i or max_q[0][1] <= min_q[0][1]:
                    _, idx = heapq.heappop(max_q)
                    max_idx = idx+1
                    continue
                
                if max_q[0][1]  == i or min_q[0][1] < max_q[0][1]:
                    _, idx = heapq.heappop(min_q)
                    max_idx = idx+1
                    continue

            ans = max(ans, i - max_idx + 1)

        return ans
