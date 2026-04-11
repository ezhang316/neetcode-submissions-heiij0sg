class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 100 99 3 2 1 200 3 3 5

        l, r = 0, len(heights) - 1

        largest = 0

        while l < r:
            current_volume = min(heights[l], heights[r]) * (r - l)
            largest = max(largest, current_volume)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return largest