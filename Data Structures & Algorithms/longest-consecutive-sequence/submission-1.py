class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = 1
        longest = 1
        nums.sort()
        for i, n in enumerate(nums[:-1]):
            if nums[i+1] == n:
                continue
            if nums[i+1] == n + 1:
                counter += 1
                longest = max(longest, counter)
            else:
                counter = 1
        return longest