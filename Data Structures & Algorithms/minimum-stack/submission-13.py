class MinStack:

    def __init__(self):
        self.stack = []
        self.currentMin = []
        self.minimum = 2**32

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum > val:
            self.minimum = val
        self.currentMin.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.currentMin.pop()
        if len(self.currentMin) > 0:
            self.minimum = self.currentMin[-1]
        else:
            self.minimum = 2**32

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin[-1]
        
        
        
