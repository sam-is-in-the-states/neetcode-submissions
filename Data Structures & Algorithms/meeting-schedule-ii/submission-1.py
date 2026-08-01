"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h = []

        for interval in intervals:
            heapq.heappush(h, (interval.start, 1))
            heapq.heappush(h, (interval.end, -1))
        
        rooms = 0
        ans = 0

        while h:
            elt = heapq.heappop(h)

            rooms += elt[1]
            ans = max(ans, rooms)

        return ans

