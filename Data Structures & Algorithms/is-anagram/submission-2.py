class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram = []
        for letter in s:
            if letter in t and s.count(letter) == t.count(letter):
                anagram.append(True)
        if len(anagram) != len(s):
            return False
        return True