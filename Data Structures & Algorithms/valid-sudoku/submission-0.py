class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in range(9):
            seen = set()

            for value in board[row]:
                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check columns
        for col in range(9):
            seen = set()

            for r in range(9):
                value = board[r][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check 3x3 boxes
        for corner_r in [0, 3, 6]:
            for corner_c in [0, 3, 6]:
                seen = set()

                for r in range(corner_r, corner_r + 3):
                    for c in range(corner_c, corner_c + 3):
                        value = board[r][c]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True

