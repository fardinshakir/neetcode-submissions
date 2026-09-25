class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for n in nums:
            if n not in numbers:
                numbers[n] = 1
            else:
                return True

        return False
