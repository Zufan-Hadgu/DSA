# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
      
        def totalsum(node):
            if not node:
                return 0
            return node.val + totalsum(node.left) + totalsum(node.right)
        total = totalsum(root)
        output = float('-inf')
        def subtree(node):
            nonlocal output
            if not node:
                return 0
            
            left = subtree(node.left)
            right = subtree(node.right)
            subtree_sum = node.val + left + right
            
            output = max(output, (total - subtree_sum) * subtree_sum)
            return subtree_sum 

        subtree(root)
        return output % (10**9 + 7)

        