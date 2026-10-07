class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0
        while left <= right:
            if heights[left] < heights[right]:
                result = heights[left]*(right-left)
            else:
                result = heights[right] * (right - left)

            if result > best:
                best = result
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best
        