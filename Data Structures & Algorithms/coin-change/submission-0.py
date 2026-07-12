class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        if amount == 0:
            return 0
        def helper(amount, coins) -> int:
            if amount in memo:
                return memo[amount]
            
            ans = float('inf')
            for coin in coins:
                if coin == amount:
                    memo[amount] = 1
                    return 1
                if coin < amount:
                    sub_ans = helper(amount - coin, coins)
                    if sub_ans == -1:
                        continue
                    ans = min(ans, 1 + sub_ans)
            
            if ans == float('inf'):
                memo[amount] = -1
            else:
                memo[amount] = ans
            
            return memo[amount]
        
        ans = helper(amount, coins)

        return memo[amount]