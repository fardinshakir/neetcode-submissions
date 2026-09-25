class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            desired = target - n
            if desired in seen:
                return [seen[desired], i]
            seen[n] = i
            
        return False