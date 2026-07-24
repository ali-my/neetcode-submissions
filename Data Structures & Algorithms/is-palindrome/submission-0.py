class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward, backward = 0, len(s) - 1
        while forward < backward:
            while forward < backward and not s[forward].isalnum():
                forward += 1
            while forward < backward and not s[backward].isalnum():
                backward -= 1
            if forward >= backward:
                return True
            if s[forward].lower() != s[backward].lower():
                return False
            forward += 1
            backward -= 1
        return True