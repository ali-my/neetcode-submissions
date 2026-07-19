class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencyDic = {}
        for num in nums:
            numFrequencyDic[num] = 1 + numFrequencyDic.get(num, 0)
        countItemsDic = [[] for i in range(len(nums) + 1)]
        for num, count in numFrequencyDic.items():
            countItemsDic[count].append(num)
        result = []
        for i in range(len(countItemsDic) -1 , 0, -1):
            for num in countItemsDic[i]:
                result.append(num)
                if len(result) == k:
                    return result;
        return result
        