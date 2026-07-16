class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        sDict = {}
        for char in s:
            if(char in sDict):
                sDict[char] += 1
            else:
                sDict[char] = 1
        for char in t:
            if(char in sDict):
                sDict[char] -= 1
                if(sDict[char] < 0):
                    return False
            else:
                return False
        return True