class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(total, total_list, start):
            if total == target:
                res.append(list(total_list))
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    break
                total_list.append(nums[i])
                dfs(total + nums[i], total_list, i)
                total_list.pop()
            
        nums.sort()
        dfs(0, [], 0)
        
        return res
            
            