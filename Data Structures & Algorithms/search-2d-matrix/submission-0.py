class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        high = len(matrix) * len(matrix[0]) - 1
        low = 0
        cols = len(matrix[0])

        while low <= high:
            mid = (low + high) // 2

            row = mid // cols
            col = mid % cols
            value = matrix[row][col]

            if target == value:
                return True
            elif target < value:
                high = mid - 1
            else:
                low = mid + 1
        return False
        