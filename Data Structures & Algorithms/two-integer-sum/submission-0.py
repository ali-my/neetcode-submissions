class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueIndexDic = {}
        for index, value in enumerate(nums):
            requiredVal = target - value
            if requiredVal in valueIndexDic:
                return [valueIndexDic[requiredVal], index]
            valueIndexDic[value] = index
        return []
