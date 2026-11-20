class MinStack:

    # The tricky part is keeping track of the mins. How to do in O(1)?
    # We need to keep track of the minimums, so that if we remove the minimum, then it's recalculated in O(1)
    # So some sort of list of mins. When we do stack.pop(), also pop from the "mins" stack if min == mins[-1]

    stack = []
    mins = []

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or (len(self.mins) > 0 and val <= self.mins[-1]):
            self.mins.append(val)    # New min since at the top of the mins stack

    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop()
        if len(self.mins) > 0 and top == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # We don't expect calls on non-empty stacks but this is safer code
        return self.mins[-1] if len(self.mins) > 0 else -1  
        
