# _83. Remove Duplicates from Sorted List


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        head_copy = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return head_copy
