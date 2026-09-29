class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for n in s:
            if n in "([{":
                stack.append(n)
            elif n in ")]}":
                if not stack:
                    return False
                
                if stack[-1] != pairs[n]:
                    return False
                stack.pop()
        return len(stack) == 0