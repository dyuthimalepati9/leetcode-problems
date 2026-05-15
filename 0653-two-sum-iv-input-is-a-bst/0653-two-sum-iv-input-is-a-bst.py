class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        vals = {}
        def helper(node):
            if not node:
                return False
            if node.val in vals:
                return True
            vals[k - node.val] = True
            return helper(node.left) or helper(node.right)
        return helper(root)