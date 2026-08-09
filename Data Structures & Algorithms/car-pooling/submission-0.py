class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        q = []
        curr = 0
        trips = sorted(trips, key=lambda x: (x[1], x[2]))
        for trip in trips:
            cnt, frm, to = trip

            while q and q[0][0] <= frm:
                _, n = heapq.heappop(q)
                curr -= n
            
            if curr + cnt > capacity:
                return False
            
            heapq.heappush(q, (to, cnt))
            curr += cnt
        return True