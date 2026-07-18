class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for s in strs:
            key = self.getAnagramUniqueKey(s)
            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(s)
        return list(anagram_groups.values())


    def getAnagramUniqueKey(self, str) -> int:
        anagramDic = [0] * 26
        for char in str:
            anagramDic[ord(char.lower()) - ord('a')] += 1
        anagramKey = 0
        for i in range(26):
            anagramKey *= 10000
            anagramKey += anagramDic[i]
        return anagramKey
