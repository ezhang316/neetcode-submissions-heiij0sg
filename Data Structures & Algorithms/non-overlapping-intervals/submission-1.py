class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0

        remove = 0

        intervals.sort()
        
        previous = intervals[0]

        for interval in intervals[1:]:
            if interval[1] <= previous[1]:
                previous = interval
                remove += 1
            else:
                if interval[0] < previous[1]:
                    remove += 1
                else:
                    previous = interval

        return remove
