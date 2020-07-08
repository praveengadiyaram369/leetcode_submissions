# _206. Reverse Linked List

# _using recursion


class Solution:

    def reversell(self, head, prev=None):

        if head is None:
            return prev

        next_node = head.next
        head.next = prev

        return self.reversell(next_node, head)

    def reverseList(self, head: ListNode) -> ListNode:

        return self.reversell(head)

# _using iterative solution


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        root = head

        while root != None:

            next_node = root.next
            root.next = prev

            prev = root
            root = next_node

        return prev


# _using stacks
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        list_stack = []
        root = head

        while root != None:
            list_stack.append(root.val)
            root = root.next

        root = head

        while root != None:
            root.val = list_stack.pop()
            root = root.next

        return head
