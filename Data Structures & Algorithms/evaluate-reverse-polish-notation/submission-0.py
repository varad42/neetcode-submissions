class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                right_int = stack.pop()
                left_int = stack.pop()
                val = left_int + right_int
                stack.append(val)
            elif i == "-":
                right_int = stack.pop()
                left_int = stack.pop()
                val = left_int - right_int
                stack.append(val)
            elif i == "*":
                right_int = stack.pop()
                left_int = stack.pop()
                val = left_int * right_int
                stack.append(val)
            elif i == "/":
                right_int = stack.pop()
                left_int = stack.pop()
                val = int(left_int / right_int)
                stack.append(val)
            else:
                stack.append(int(i))

        return stack[-1]
        