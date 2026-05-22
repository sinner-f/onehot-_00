class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        def is_pal(right:Optional[ListNode]) ->bool:
            if right.next and not is_pal(right.next):
                return False
            nonlocal left
            if left.val != right.val:
                return False
            left = left.next
            return True
        return is_pal(head)