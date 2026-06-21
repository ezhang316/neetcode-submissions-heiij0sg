class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0

        max_left, max_right = 0, 0

        l, r = -1, len(height)

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]
        
        return res
