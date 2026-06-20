class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0 for _ in range(len(height))]
        max_right = [0 for _ in range(len(height))]

        current_max = 0
        for i in range(len(height)):
            max_left[i] = current_max
            current_max = max(current_max, height[i])
        
        current_max = 0
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = current_max
            current_max = max(current_max, height[i])
        
        total = 0
        for i in range(len(height)):
            print(min(max_left[i], max_right[i]))
            total += max(min(max_left[i], max_right[i]) - height[i], 0)
        
        return total
        

