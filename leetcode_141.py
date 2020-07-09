# _141. Linked List Cycle


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False