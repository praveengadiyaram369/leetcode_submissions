# _234. Palindrome Linked List


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if head is None or head.next is None:
            return True

        stack = []
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.val)
            if fast:
                slow = slow.next

        while slow.next:
            slow = slow.next
            if slow.val != stack.pop():
                return False
        return True
