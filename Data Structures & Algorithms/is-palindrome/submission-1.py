class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        result = ""

        for c in s:
            if c.isalnum():
                result += c
            else:
                continue

        return result.lower() == result[::-1].lower()