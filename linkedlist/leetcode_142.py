class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None
