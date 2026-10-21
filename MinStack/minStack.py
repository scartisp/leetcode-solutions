class MinStack:

    def __init__(self):
        self.stack = []
        self.minValues = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        
        if len(self.minValues) == 0 or value <= self.minValues[-1]:
            self.minValues.append(value)

    def pop(self) -> None:
        if self.top() == self.minValues[-1]:
            self.minValues.pop()
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValues[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
