class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        sell = prices[0]

        for p in prices:
            if p < buy:
                ans = max(ans, sell - buy)
                buy = p
                sell = p
            if p > sell:
                sell = p
        return max(ans, sell - buy)