"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from operator import attrgetter

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        max_rooms = 0

        min_heap = []

        intervals.sort(key=attrgetter('start', 'end'))
        for i in intervals:

            if min_heap:
                while min_heap and min_heap[0] <= i.start:
                    heapq.heappop(min_heap)

            heapq.heappush(min_heap, i.end)
                
            max_rooms = max(max_rooms, len(min_heap))
        
        return max_rooms