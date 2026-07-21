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
            elif zero_count == 1:
                if i == zero_index:
                    products = [0] * len(nums)
                    products[zero_index] = left_product
                else:
                    products[zero_index] *= nums[i]
            else:
                products[i] *= left_product
                left_product *= nums[i]
        
        if zero_count == 1:
            return products

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]

        return products