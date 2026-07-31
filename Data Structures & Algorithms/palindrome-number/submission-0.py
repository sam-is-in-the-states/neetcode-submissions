class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        res = 0

        while temp:
            d = temp % 10
            temp //= 10
            res = 10*res + d

        return x == res
        