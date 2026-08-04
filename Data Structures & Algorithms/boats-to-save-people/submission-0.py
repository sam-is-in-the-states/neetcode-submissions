class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        n = len(people)
        l = 0
        r = n-1
        ans = 0

        while l <= r:
            ans += 1

            if people[l] + people[r] > limit:
                r -= 1
            else:
                r -= 1
                l += 1
        return ans
