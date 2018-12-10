class StackIntNumbers(object):
    """ Implement a stack of integers in which the operation of adding, removing, and finding
    the maximum value has a constant runtime.
    """

    def __init__(self):
        self.stack = []
        self._max = None

    def push(self, number):
        if self._max is None:
            self._max = number
        elif self._max < number:
            self._max = number
        self.stack.append(number)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if not self.emtpy():
            return self.stack[-1]

    def emtpy(self):
        return self.stack == []

    def max(self):
        return self._max


stack = StackIntNumbers()
stack.push(3)
stack.push(10)
stack.push(1)

assert stack.max() == 10
assert stack.pop() == 1
assert stack.top() == 10
assert not stack.emtpy()
