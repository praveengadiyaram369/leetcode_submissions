# _160. Intersection of Two Linked Lists


class Solution:

    def get_ll_len(self, head):

        if head is None:
            return 0
        return 1 + self.get_ll_len(head.next)

    def skip_diff(self, head, diff):
        for i in range(diff):
            head = head.next
        return head

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        lenA = self.get_ll_len(headA)
        lenB = self.get_ll_len(headB)

        if lenA and lenB:
            if lenA > lenB:
                headA = self.skip_diff(headA, lenA - lenB)
            elif lenB > lenA:
                headB = self.skip_diff(headB, lenB - lenA)

            while headA:
                if headA == headB:
                    return headA

                headA = headA.next
                headB = headB.next

            return None

        return None
