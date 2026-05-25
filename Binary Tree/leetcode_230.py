class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node:Optional[TreeNode]) -> None:
            nonlocal k,ans
            if node is None or k <= 0:
                return
            dfs(node.left)
            k -= 1
            if k == 0:
                ans = node.val
            dfs(node.right)
        dfs(root)
        return ans