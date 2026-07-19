class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencyDic = {}
        for num in nums:
            if num not in numFrequencyDic:
                numFrequencyDic[num] = 0
            numFrequencyDic[num] += 1
        result = []
        sorted_items = sorted(numFrequencyDic.items(), key=lambda item: item[1], reverse=True)
        for i in range(min(k, len(sorted_items))):
            result.append(sorted_items[i][0])
        return result
        