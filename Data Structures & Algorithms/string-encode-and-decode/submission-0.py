class Solution:
    divider_char = '~'
    def encode(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + self.divider_char + s 
        return encoded_str


    def decode(self, s: str) -> List[str]:
        result = []
        if s is None or len(s) == 0:
            return result
        start_index = 0
        i = 0
        while i < len(s):
            if s[i] == self.divider_char:
                length = self.castToInt(s[start_index:i])
                result.append(s[i + 1:i + 1 + length])
                start_index = i + 1 + length
                i = start_index
            i += 1
        return result


    def castToInt(self, s: str) -> int:
        result = 0
        for char in s:
            result = result * 10 + (ord(char) - ord('0'))
        return result