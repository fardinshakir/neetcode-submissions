class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s.lower() if c.isalnum())
        reversed = s[::-1]
        if reversed == s:
            return True
        else:
            return False
