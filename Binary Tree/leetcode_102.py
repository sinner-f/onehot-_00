class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])#collections.deque 的构造函数要求传入的参数必须是可迭代对象（如列表、元组、字符串等）。
        # 而你的 root 是一个 TreeNode 对象（树的节点），它本身不是可迭代的。所以不可以写成q = deque(root)
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)
        return ans
