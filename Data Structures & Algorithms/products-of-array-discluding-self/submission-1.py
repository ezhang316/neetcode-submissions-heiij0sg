class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_product = ["None"]
        for i in range(1, len(nums)):
            cumulative = left_product[-1]
            if cumulative != "None":
                left_product.append(cumulative * nums[i - 1])
            else:
                left_product.append(nums[0])

        right_product = ["None"]
        for i in range(len(nums) - 1, 0, -1):
            cumulative = right_product[0]
            if cumulative != "None":
                right_product.insert(0, cumulative * nums[i])
            else:
                right_product.insert(0, nums[i])
        
        result = []
        
        print(left_product)
        print(right_product)

        for i in range(len(nums)):
            if left_product[i] == "None":
                result.append(right_product[i])
            elif right_product[i] == "None":
                result.append(left_product[i])
            else:
                result.append(left_product[i] * right_product[i])
        
        return result
            