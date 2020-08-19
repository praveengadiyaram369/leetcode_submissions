# _155. Min Stack


class MinStack:

    def __init__(self):
        self.head = Node(None, None, None)

    def push(self, x: int) -> None:
        if self.head.min is None:
            self.head.val = x
            self.head.min = x
        else:
            new_node = Node(x, min(x, self.head.min), self.head)
            self.head = new_node

    def pop(self) -> None:
        self.head = self.head.next
        if self.head is None:
            self.head = Node(None, None, None)

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


class Node:

    def __init__(self, val, minimum, next_node):
        self.val = val
        self.min = minimum
        self.next = next_node
