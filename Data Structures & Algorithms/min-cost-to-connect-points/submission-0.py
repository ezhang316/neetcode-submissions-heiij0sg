class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        mh = []
        in_graph = set()
        x1, y1 = points.pop()
        in_graph.add((x1, y1))
        res = 0
        for _ in range(len(points)):
            for i in range(len(points)):
                x2, y2 = points[i]
                heapq.heappush(mh, (abs(x1 - x2) + abs(y1 - y2), (x1, y1), (x2, y2)))

            cost, point1, point2 = heapq.heappop(mh)
            while point1 in in_graph and point2 in in_graph:
                cost, point1, point2 = heapq.heappop(mh)
            
            res += cost
            if point1 not in in_graph:
                in_graph.add(point1)
                x1, y1 = point1
            else:
                in_graph.add(point2)
                x1, y1 = point2
            
        return res