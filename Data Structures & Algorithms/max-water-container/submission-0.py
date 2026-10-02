class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            new_area = (right - left) * min(heights[left], heights[right]) 
            if new_area > area:
                area = new_area
            if heights[right] > heights[left]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return area
            