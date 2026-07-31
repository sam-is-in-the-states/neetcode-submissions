class Solution:
    def reverse(self, x: int) -> int:
        mul = -1 if x < 0 else 1
        x = -x if x < 0 else x

        max_val = 2**31
        print(max_val)

        temp = x
        res = 0

        while temp > 0:
            d = temp % 10
            temp //= 10

            if (max_val - d) // 10 < res:
                return 0
            
            res = 10 * res + d

        if mul == -1 and res == max_val:
            return 0

        return res * mul