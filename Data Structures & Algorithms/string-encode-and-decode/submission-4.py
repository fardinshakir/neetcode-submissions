class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(str(len(word)))
            result.append('#')
            result.append(word)
            #result += str(len(word)) + '#' + word THIS IS WORST CASE o(n^2)
        return "".join(result)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i + length])
            i += length

        return result