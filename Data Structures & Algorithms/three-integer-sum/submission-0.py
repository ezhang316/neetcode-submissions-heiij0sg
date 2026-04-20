class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each num in nums
        # check the rest of the list for if two numbers put together equal
        # the negative of the current number
        # O(n^2)

        result = []

        for i in range(len(nums)):
            i_num = nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                j_num = nums[j]
                goal = -(i_num + j_num)

                for k in range(len(nums)):
                    if k == i or k == j:
                        continue
                    k_num = nums[k]
                    if k_num == goal:
                        triplet = [i_num, j_num, k_num]
                        triplet.sort()
                        if triplet not in result:
                            result.append(triplet)
        
        return result