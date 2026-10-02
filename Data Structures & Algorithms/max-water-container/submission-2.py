class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        biggest_area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right]) 
            biggest_area = max(area, biggest_area)

            if heights[right] > heights[left]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return biggest_area