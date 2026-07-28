ListNode.__lt__ = lambda a, b: a.val < b.val#这行代码是为了将 ListNode “改造”成可比较的对象，并指定按数值大小排序，使得 heapq 模块能够正确地维护堆结构，保证每次弹出的节点都是当前所有链表头节点中值最小的那个。


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        h = [head for head in lists if head]
        heapify(h)
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next
