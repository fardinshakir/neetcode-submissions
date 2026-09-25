class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            desired = target - n
            if desired in nums:
                return [i, nums.index(desired)]
        return False