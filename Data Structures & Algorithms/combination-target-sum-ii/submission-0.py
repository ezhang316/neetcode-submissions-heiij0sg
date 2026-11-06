class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort()
        res = []
        current_candidates = []

        def dfs(current_target, i):
            if i >= len(candidates):
                return

            if current_target == candidates[i]:
                current_candidates.append(candidates[i])
                copy = current_candidates.copy()
                res.append(copy)
                current_candidates.pop()
            
            if candidates[i] < current_target:
                current_candidates.append(candidates[i])
                dfs(current_target - candidates[i], i + 1)
                current_candidates.pop()
            i += 1
            while i < len(candidates) and candidates[i - 1] == candidates[i]:
                i += 1
            dfs(current_target, i)
        
        dfs(target, 0)

        return res

