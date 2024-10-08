class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min (val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# - we select minStack[-1] only when it already exists 
# - we pop minStack also as if the main popped value wasn't min, even then the prev val in minStack will be correct

# TC - 1
# SC - 1 
