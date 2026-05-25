class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)       # 左
            ans.append(node.val) # 根（这行代码移到前面就是前序，移到后面就是后序）
            dfs(node.right)      # 右

        ans = []
        dfs(root)
        return ans

