class MinStack:

    def __init__(self):
        self.stack = []
        self.min_Stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_Stack) == 0:
            self.min_Stack.append(val)
        elif self.min_Stack[-1] > val:
            self.min_Stack.append(val)
        else:
            self.min_Stack.append(self.min_Stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_Stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_Stack[-1]

