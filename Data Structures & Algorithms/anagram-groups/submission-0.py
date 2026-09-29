class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_ = ''.join(sorted(word))
            anagrams[sorted_].append(word)


        return list(anagrams.values())