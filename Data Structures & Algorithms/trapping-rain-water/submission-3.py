class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0

        def left_max_list(heights):
            n = len(heights)
            left_max = [0] * n
            left_max[0] = heights[0]

            for i in range(1, n):
                left_max[i] = max(left_max[i - 1], heights[i])

            return left_max

        def right_max_list(heights):
            n = len(heights)
            right_max = [0] * n
            right_max[n - 1] = heights[n - 1]

            for i in range(n - 2, -1, -1):
                right_max[i] = max(right_max[i + 1], heights[i])

            return right_max

        if len(height) < 3:
            return 0

        left_max = left_max_list(height)
        right_max = right_max_list(height)

        for i in range(1, len(height) - 1):
            water = min(left_max[i], right_max[i]) - height[i]
            total_water += water

        return total_water

        