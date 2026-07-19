class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = {}
        if amount == 0:
            return 1

        def helper(amount, coins, idx) -> int:
            if idx == len(coins):
                return 0        

            if amount < 0:
                return 0
            
            if amount == 0:
                return 1

            if (amount, idx) in m:
                return m[(amount, idx)]
            
            ans = 0
            ans += helper(amount - coins[idx], coins, idx)
            ans += helper(amount, coins, idx+1)
            m[(amount, idx)] = ans
            return ans
        
        helper(amount, list(set(coins)), 0)
        return m[(amount,0)]
            

            
