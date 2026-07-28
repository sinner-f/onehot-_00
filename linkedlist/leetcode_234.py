class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        def is_pal(right:Optional[ListNode]) ->bool:
            if right.next and not is_pal(right.next):
                return False
            nonlocal left#nonlocal 是 Python 3 引入的一个关键字，用于在嵌套函数（闭包）中，声明一个变量属于“外层非全局函数”的作用域，从而允许你修改它。
            if left.val != right.val:
                return False
            left = left.next
            return True
        return is_pal(head)