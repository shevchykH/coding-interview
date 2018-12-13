class StackIntNumbers(object):
    """ Implement a stack of integers in which the operation of adding, removing, and finding
    the maximum value has a constant runtime.
    """

    def __init__(self):
        self.stack = []
        self.track_stack = []
        self._max = None

    def push(self, element):
        if self._max is None:
            self._max = element
            self.stack.append(element)
            self.track_stack.append(element)

        elif self._max < element:
            self._max = element
            self.stack.append(element)
            self.track_stack.append(element)
        else:
            self.stack.append(element)

    def pop(self):
        element = self.stack.pop()
        if element == self._max:
            self.track_stack.pop()
            self._max = self.max()
        return element

    def top(self):
        if not self.emtpy():
            return self.stack[-1]

    def emtpy(self):
        return self.stack == []

    def max(self):
        if self.track_stack:
            return self.track_stack[-1]


stack = StackIntNumbers()
stack.push(3)
stack.push(10)
stack.push(12)
stack.push(1)
stack.pop()
stack.pop()
stack.push(12)
stack.push(1)


assert stack.max() == 12
assert stack.pop() == 1
assert stack.pop() == 12
assert stack.max() == 10
assert not stack.emtpy()
