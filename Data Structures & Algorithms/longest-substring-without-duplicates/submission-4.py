class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = {}
        max_length = 0

        while right < len(s):

            while s[right] in seen:
                del seen[s[left]]
                left += 1

            seen[s[right]] = 1
            max_length = max(max_length, len(seen))
            right += 1
            
        return max_length