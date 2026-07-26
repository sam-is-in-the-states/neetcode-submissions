class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x:x[0])

        curr = None
        for item in intervals:
            if curr == None:
                curr = item
                continue
            
            if curr[1] < item[0]:
                res.append(curr)
                curr = item
                continue
            
            curr[1] = max(curr[1], item[1])
        
        if curr:
            res.append(curr)
        return res