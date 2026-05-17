class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []

        prev = None

        for i, j in intervals:
            if not prev:
                prev = [i,j]
                continue
            prev_i, prev_j = prev

            if i <= prev_j:
                prev[1] = j
            else:
                res.append(prev)
                prev = [i,j]
            
            
        res.append(prev)

        return res