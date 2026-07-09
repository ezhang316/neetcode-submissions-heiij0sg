class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush_max(res, (distance,point))

            if len(res) > k:
                heapq.heappop_max(res)
        
        final_res = []
        for tup in res:
            final_res.append(tup[1])
        
        return final_res