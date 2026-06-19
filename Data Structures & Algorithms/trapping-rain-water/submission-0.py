class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        st_idx = 0
        curr_max_height = 0
        running_sum = 0

        for idx, h in enumerate(height):
            if h >=  curr_max_height:
                ans += (idx - st_idx) * curr_max_height - running_sum
                curr_max_height = h
                st_idx = idx
                running_sum = h
            else:
                running_sum += h
        
        height = height[st_idx:][::-1]

        st_idx = 0
        curr_max_height = 0
        running_sum = 0

        for idx, h in enumerate(height):
            if h >=  curr_max_height:
                ans += (idx - st_idx) * curr_max_height - running_sum
                curr_max_height = h
                st_idx = idx
                running_sum = h
            else:
                running_sum += h

        return ans
        