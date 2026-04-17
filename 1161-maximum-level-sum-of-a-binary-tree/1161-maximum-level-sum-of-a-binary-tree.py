# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = -1
        max_sum = float('-inf')
        curr_idx = 0
        que = deque([root])
        while que:
            curr_idx += 1
            curr_sum = 0
            tmp = deque()
            for node in que:
                curr_sum += node.val
                if node.right is not None:
                    tmp.append(node.right)
                if node.left is not None:
                    tmp.append(node.left)
            if curr_sum > max_sum:
                max_sum = curr_sum
                res = curr_idx
            que = tmp
        return res
           