class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in nums:
                counter = 1

                while n + counter in nums:
                    counter += 1

                longest = max(longest, counter)

        return longest