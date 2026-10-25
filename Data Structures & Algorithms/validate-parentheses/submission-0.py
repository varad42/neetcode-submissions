class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == bracket[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        