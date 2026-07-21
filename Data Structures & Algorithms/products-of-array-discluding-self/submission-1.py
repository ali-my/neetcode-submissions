class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        left_product = 1
        zero_count = 0
        zero_index: -1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                zero_index = i
            if zero_count > 1:
                return [0] * len(nums)
            products[i] *= left_product
            left_product *= nums[i]
        
        if zero_count == 1:
            result = [0] * len(nums)
            result[zero_index] = products[zero_index]
            for i in range(zero_index + 1, len(nums)):
                result[zero_index] *= nums[i]
            return result

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]

        return products