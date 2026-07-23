class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestConsecutive = 0
        for i in range(len(nums)):
            if nums[i] in numSet:
                length = 1
                num = nums[i] + 1
                while num in numSet:
                    length += 1
                    num += 1
                if length > longestConsecutive:
                    longestConsecutive = length
        return longestConsecutive