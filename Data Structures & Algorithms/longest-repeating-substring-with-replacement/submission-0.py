class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        seen = {}
        longest_character = 0
        while right < len(s):
            if s[right] not in seen:
                seen[s[right]] = 1
            else:
                seen[s[right]]  += 1
            
            max_item = max(seen.values())
            while (right - left + 1) - max_item > k:
                seen[s[left]] -= 1
                left += 1
            longest_character = max(longest_character, (right - left + 1))
            right += 1
        return longest_character