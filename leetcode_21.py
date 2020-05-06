# _21. Merge Two Sorted Lists


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        curr = None
        temp = None
        head = None

        if l1 and l2:

            while l1 and l2:
                if l1.val <= l2.val:
                    temp = l1
                    l1 = l1.next
                else:
                    temp = l2
                    l2 = l2.next

                if curr:
                    curr.next = temp
                    curr = curr.next
                else:
                    head = temp
                    curr = head

            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
        else:
            if l1:
                return l1
            elif l2:
                return l2

        return head
