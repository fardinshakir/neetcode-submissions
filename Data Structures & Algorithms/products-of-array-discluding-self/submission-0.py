class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        left_product = 1
        for i in range(len(nums)):
            output[i] = left_product
            left_product = left_product*nums[i]          

        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * right_product
            right_product = right_product*nums[i]
        return output