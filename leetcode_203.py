# _203. Remove Linked List Elements


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return head

        head_copy = head
        cur = head

        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
                continue

            cur = cur.next

        return head_copy
