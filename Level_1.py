class MinMaxStack:
    def __init__(self):
        self.stack = []  # Stores the actual stack values
        self.min_stack = []  # Stores the minimum values
        self.max_stack = []  # Stores the maximum values

    def push(self, x):
        self.stack.append(x)
        # Update min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
        # Update max_stack
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if not self.stack:
            raise IndexError("Pop from empty stack")
        self.stack.pop()
        self.min_stack.pop()
        self.max_stack.pop()

    def top(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]

    def getMax(self):
        if not self.max_stack:
            raise IndexError("Stack is empty")
        return self.max_stack[-1]

# Demonstration of all possible use cases
if __name__ == "__main__":
    s = MinMaxStack()
    s.push(5)
    s.push(2)
    s.push(8)
    s.push(1)
    s.push(10)
    print("Top element:", s.top())      # Output: 10
    print("Minimum element:", s.getMin())  # Output: 1
    print("Maximum element:", s.getMax())  # Output: 10
    s.pop()
    print("Top after pop:", s.top())    # Output: 1
    print("Min after pop:", s.getMin())  # Output: 1
    print("Max after pop:", s.getMax())  # Output: 8
