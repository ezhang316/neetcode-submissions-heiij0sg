class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        mh = []
        
        for i in range(k):
            heapq.heappush_max(mh, nums[i])

        l = 0
        r = k
        remove = defaultdict(int)
        res = []
        while r < len(nums):
            res.append(mh[0])
            remove[nums[l]] += 1
            l += 1
            while mh and mh[0] in remove and remove[mh[0]] != 0:
                remove[mh[0]] -= 1
                heapq.heappop_max(mh)
            heapq.heappush_max(mh, nums[r])
            r += 1

        res.append(mh[0])
        
        return res