class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0 for _ in range(len(temperatures))]
        warmer_not_found = []

        for i in range(len(temperatures)):
            if warmer_not_found:
                while warmer_not_found and warmer_not_found[-1][0] < temperatures[i]:
                    temp = warmer_not_found.pop()
                    res[temp[1]] = i - temp[1]
            
            warmer_not_found.append((temperatures[i], i))
        
        return res