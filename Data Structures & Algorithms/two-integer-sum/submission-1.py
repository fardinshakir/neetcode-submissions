class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i,test in enumerate(nums):
            check = target - test
            if check in values:
                return [values[check], i]
            
            values[test] = i