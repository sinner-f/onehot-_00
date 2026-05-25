class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            ans.append(cur[-1].val)
            nxt = []
            for node in cur:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
        return ans
